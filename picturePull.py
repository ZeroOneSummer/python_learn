from contextlib import closing
import requests, json, time
from tqdm import tqdm
from bs4 import BeautifulSoup

class down_picture(object):

    def __init__(self):
        self.server = 'https://unsplash.com/photos/xxx/download?force=trues'    # 图片ID替换xxx
        self.target = 'http://unsplash.com/napi/feeds/home'
        self.photos_id = []
        self.headers = {'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
        self.path = 'C:\\Users\\v_pijiang\\Desktop\\'

    # 图片ID
    def get_ids(self):
        next_page = self.target
        self.get_html_resp(next_page)
        time.sleep(1)   # 模拟人工请求间隔
        for i in range(20):
            self.get_html_resp(next_page)

    # 获取json响应
    def get_html_resp(self, _url):
        req = requests.get(url=_url, headers=self.headers, verify=False)    # verify关闭SSL验证，防爬虫
        htmlJson = json.loads(req.text)
        _url = htmlJson['next_page']
        for each in htmlJson['photos']:
            self.photos_id.append(each['id'])
        time.sleep(1)

    # 下载图片
    def download(self, photo_id, file_no):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        target = self.server.replace('xxx', photo_id)
        with closing(requests.get(url=target, stream=True, verify=False, headers=self.headers)) as r:
            with open(self.path+'%d.jpg' % file_no, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    obj = down_picture()
    print('获取图片连接中:')
    obj.get_ids()
    print('图片下载中>>>')
    for i in tqdm(range(len(obj.photos_id))):
        obj.download(obj.photos_id[i], (i+1))
