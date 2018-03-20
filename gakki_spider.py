import requests
from bs4 import BeautifulSoup

import random
import time
import os

def getHtmlText(url, code = "utf-8"):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }

    try:
        r = requests.get(url,headers = headers)
        r.encoding  = code
        r.raise_for_status()
    except:
        return ""
    return r.text

def parse(html):
    pics_source = set()
    soup = BeautifulSoup(html,"html.parser")
    content = soup.find("ul",class_="poster-col3 clearfix")
    pics = content.find_all("img")
    next_page_url = soup.find("span",class_="next").find("a").get("href")

    for pic in pics:
        pics_source.add(pic["src"])

    return pics_source,next_page_url
    
def page_turn(url):
    picture_list = set() #图片集合
    currentUrl = url
    count = 1
    while(count) <=60:
        html = getHtmlText(currentUrl)
        pics, nextUrl = parse(html)
        picture_list = picture_list | pics
        currentUrl = nextUrl
        count = count + 1

    return picture_list

def download_pic(imgs):
    count = 1
    
    for img in imgs:
        r = requests.get(img)
        path = "E:\python3\spider\pics\\" + str(count) +".jpg"
        with open(path,'wb') as f:
            try:
                f.write(r.content)
                print(count)
                count = count + 1
            except:
                print("下载失败")

if __name__ == '__main__':
    url = "https://movie.douban.com/celebrity/1018562/photos/"
    imgs = page_turn(url)
    download_pic(imgs)

