import requests, re, os, uuid, urllib3, json
from tqdm import tqdm
from lxml.html import etree

class movie_download(object):

    def __init__(self):
        self._target_url = "https://www.dy2018.com"
        self._detail_url = "https://www.dy2018.com/x/index_#.html"
        self._save_base = "C:\\Users\\Administrator\\Desktop\\movie\\"
        self._headers = {}
        self._type_name_arr = []    # 类型电影-分页
        self._type_url_arr = []     # 类型名称
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

    # 创建分类目录并下载
    def down_movie(self, _object):
        # 获取电影分类
        _object.get_movie_type()
        # 创建分类目录并下载
        for i in tqdm(range(len(self._type_url_arr))):
            _type_name = self._type_name_arr[i]
            print("\n-> 【%s】" % _type_name)
            # 创建类型目录
            _object.create_dir(_type_name)
            _type_url = self._type_url_arr[i]
            _type_resp = requests.get(url=_type_url)
            _type_resp.encoding = _type_resp.apparent_encoding
            _type_html = etree.HTML(_type_resp.text)
            _type_text = _type_html.cssselect('.x p')[0].text
            _total_page = re.findall(r'/(.*?) ', _type_text)[0]
            # 分页页面
            for j in range(1, int(_total_page)):
                if j == 1:
                    _page_url = _type_url + "index.html"
                else:
                    _page_url = _type_url + "index_" + str(j) + ".html"
                _page_resp = requests.get(url=_page_url)
                _page_resp.encoding = _page_resp.apparent_encoding
                _page_html = etree.HTML(_page_resp.text)
                _detail_list = _page_html.cssselect('.co_content8 .tbspan b .ulink:nth-child(even)')
                for item in _detail_list:
                    # 磁力url
                    _detail_href = item.attrib['href']
                    _magnet_url = self._target_url + _detail_href
                    _magnet_resp = requests.get(url=_magnet_url)
                    _magnet_resp.encoding = _magnet_resp.apparent_encoding
                    _down_html = etree.HTML(_magnet_resp.text)
                    _down_name = re.findall(r'《(.*?)》', item.attrib['title'])[0]
                    _magnet_down_url = _down_html.cssselect('#downlist tbody a')[0].attrib['href']
                    _mp4_href = _down_html.cssselect('#Zoom .player_list li a')[0].attrib['href']
                    _mp4_down_url = re.findall(r'ftp:.*.mp4$', _mp4_href, re.M)[0]

                    print("->> ", _down_name)
                    print("->> ", _magnet_down_url)
                    print("->> ", _mp4_down_url)

                    _file_path = self._save_base + _type_name + '\\' + _down_name + '.txt'
                    with open(_file_path, 'a', encoding='utf-8') as file:
                        file.writelines(_magnet_down_url)
                        file.write('\n')
                        file.writelines(_mp4_down_url)
                        file.write('\n\n')

    # 创建目录
    def create_dir(self, _type_name):
        _save_dir = self._save_base + _type_name
        if not os.path.exists(_save_dir):
            os.makedirs(_save_dir)




# Test
if __name__ == "__main__":
    obj = movie_download()
    obj.down_movie(obj)


