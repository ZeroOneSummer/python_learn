import os
from contextlib import closing
from tqdm import tqdm
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests, json, time

class down_picture(object):

    def __init__(self):
        self.target = 'https://unsplash.com/napi/photos?page=xxx'    # 页码
        self.photo_id = []
        self.down_url = []
        self.save_path = 'C:\\Users\\v_pijiang\\Desktop\\photos\\'
        self.page = 10  # 下载页数

    # 从json获取下载地址
    def get_down_url(self):
        totol_page = self.page
        for page in range(1, totol_page):
            req_url = self.target.replace('xxx', str(page))
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 抑制证书警告
            resp_json = requests.get(url=req_url, verify=False, allow_redirects=False)  # verify关闭SSL验证，防爬虫
            _arrays = json.loads(resp_json.text)
            for item in _arrays:
                self.photo_id.append(item['id'])
                self.down_url.append(item['links']['download'])
            time.sleep(1)

    # 下载图片
    def download(self):
        _headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        for i in tqdm(range(len(self.photo_id))):
            with closing(requests.get(url=self.down_url[i], stream=True, verify=False, headers=_headers)) as r:
                with open(self.save_path + '%s.jpg' % self.photo_id[i], 'ab+') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()

    # 创建目录
    def create_dir(self):
        _path = self.save_path
        if not os.path.exists(_path):  # 判断文件夹是否已经存在
            os.mkdir(_path)
            print(_path + ' 目录创建成功')
        else:
            print(_path + ' 目录已存在')


if __name__ == '__main__':
    obj = down_picture()
    print('获取图片连接中:')
    obj.create_dir()
    obj.get_down_url()
    print('图片下载中>>>')
    obj.download()

