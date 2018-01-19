import requests

class HtmlDownloader(object):
    def download(self,url,code = "utf-8"):
        try:
            header={
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.8",
        "Connection" : "keep-alive",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
        }
            r = requests.get(url,headers = header,timeout = 30)
            r.raise_for_status()
            r.encoding = code
            return r.text
        except:
            print("download failed")
            return ""
