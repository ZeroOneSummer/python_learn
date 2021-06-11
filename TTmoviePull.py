import np as np
import requests, re, os, uuid, urllib3, json
from tqdm import tqdm
from lxml.html import etree

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, time):
            return obj.__str__()
        else:
            return super(MyEncoder, self).default(obj)

class movie_download(object):

    def __init__(self):
        self._target_url = "https://www.dy2018.com"
        self._headers = {}
        self._type_url_arr = []
        self._type_name_arr = []
        self._url_arr = []
        self._name_arr = []

    # 获取电影分类
    def get_movie_type(self):
        _resp = requests.get(url=self._target_url)
        _resp.encoding = _resp.apparent_encoding
        _html = etree.HTML(_resp.text)
        _a_list = _html.cssselect('#menu li > a')
        for i in range(len(_a_list)-8):
            self._type_url_arr.append(self._target_url + _a_list[i].attrib['href'])
            self._type_name_arr.append(_a_list[i].text)


    # 获取电影名称
    def get_movie_info(self, _object):
        _object.get_movie_type()
        print(json.dumps(self, cls=MyEncoder, indent=4))
        for item in self._type_url_arr:
            print(item)


# Test
if __name__ == "__main__":
    obj = movie_download()
    obj.get_movie_info(obj)