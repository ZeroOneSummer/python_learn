import requests
from bs4 import BeautifulSoup

_url = 'http://www.cntour.cn'
_responseHtml = requests.get(_url)
# 解析html
_soup = BeautifulSoup(_responseHtml.text, 'lxml')
_data = _soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(_data)
