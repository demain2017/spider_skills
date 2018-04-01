import requests
from bs4 import BeautifulSoup
import json
import random
import time

def get_one_page(url):
    headers = {
         'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    try:
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        return r.text
    except:
        print('error')


def parse_one_page(html):
    soup = BeautifulSoup(html,"html.parser")
    contents = soup.find_all('dd')
    for content in contents:
        index = content.find('i').string #排名
        image = content.find('img')['src'] #图片地址
        film = content.find('p', class_ = 'name').string #电影名
        actor = content.find('p', class_ = 'star').string.strip() #演员
        time = content.find('p', class_ = 'releasetime').string.strip() #发布日期
        score = content.find('i', class_ = 'integer').string + content.find('i', class_='fraction').string #评分
        #print(image,film_name,actor,time,score)
        yield {
            "index" : index,
            "image" : image,
            "film" : film,
            "actor" : actor,
            "time" : time,
            "score" : score
        }  

def write_to_file(content):
    with open('result.txt', 'a', encoding = 'utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii = False) + '\n') #调用json库的dumps()实现字典的序列化


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for content in parse_one_page(html):
        print(content)
        write_to_file(content)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i * 10)
        time.sleep(random.random())
