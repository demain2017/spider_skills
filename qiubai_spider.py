import requests
from bs4 import BeautifulSoup
import os
import time
import random
import re

#获取网页
def get_html(url, code = "utf-8"):
    header = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.8",
        "Connection" : "keep-alive",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
            }
    try:
        r = requests.get(url, headers = header)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

#从网页中获取数据
def get_data(html):
    datas = [] #存放最终数据
    pictures = [] #存放作者头像
    bs = BeautifulSoup(html, "html.parser")
    body = bs.body 
    content_left = body.find('div', id='content-left') #找到主体框
    articles = content_left.find_all('div', attrs = {'class':re.compile('article block untagged mb15')}) #获得主体框的各个文章信息
    
    pages = content_left.find('ul', class_ = 'pagination') #获得翻页框
    next_pageUrl = pages.find('span',class_='next').find_parent('a').get('href') #获取换页的URL
    
    for article in articles:
        temp = [] #存放临时信息
        author_name = article.find('div', class_ = 'author clearfix').find('h2').string #获得作者名字
        author_pic = article.find('div', class_ = 'author clearfix').find('img').get('src') #获得作者头像
        pictures.append(author_pic)
        content = article.find('div', class_ = 'content').find('span').string #文章的内容
        stats = article.find_all('i',class_='number')
        funnys = stats[0].string + 'funny' #好笑数量
        comments = stats[1].string + 'comment' #评论数量
        #依次将作者名字，作者头像，文章内容，笑脸数，评论数添加到临时列表中
        temp.append(author_name)
        temp.append(author_pic)
        temp.append(content)
        temp.append(funnys)
        temp.append(comments)
        #将临时列表添加进最终列表中
        datas.append(temp)
    return datas,pictures,next_pageUrl
def write_data(datas):
    pass

def download_pic(imgs):
    pass


if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/'
    html = get_html(url)
    get_data(html)
