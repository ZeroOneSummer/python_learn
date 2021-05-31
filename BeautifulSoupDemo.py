import requests
from bs4 import BeautifulSoup
import re
import time

_url = 'http://www.cntour.cn'
'''
 伪装请求头，防止反爬虫识别
'''
_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
_responseHtml = requests.get(_url, headers=_headers)
# 解析html
_soup = BeautifulSoup(_responseHtml.text, 'lxml')
_data = _soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
# print(_data)

# 遍历
for item in _data:
    _rs = {
        'title': item.get_text(),
        'link': item.get('href'),
        'id': re.findall('\d+', item.get('href'))
    }

time.sleep(1)  # 休眠
print(_rs)
