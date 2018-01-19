from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/item/(.*)'))
        url_head = "https://baike.baidu.com"
        for link in links:
            new_url = link['href']
            new_full_url = url_head + new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}
        
        res_data['url'] = page_url
        title_node = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find('h1').string
        res_data['title'] = title_node
        summary_node = soup.find('div',class_ = 'lemma-summary').get_text()
        res_data['summary'] = summary_node

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
