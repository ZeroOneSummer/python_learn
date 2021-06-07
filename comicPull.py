import os
import re
import time
from contextlib import closing

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class down_comic(object):

    def __init__(self):
        self.target_url = "https://www.dmzj.com/info/yaoshenji.html"
        self.base_down_url = "https://images.dmzj.com/img/chapterpic/"
        self.chapter_names = []
        self.chapter_urls = []
        self.save_path = 'C:\\Users\\v_pijiang\\Desktop\\comic\\'

    def create_dir(self, _dir_path):
        if not os.path.exists(_dir_path):
            os.makedirs(_dir_path)

    # 获取动漫章节链接和章节名
    def get_chapter(self):
        r = requests.get(url=self.target_url)
        bs = BeautifulSoup(r.text, 'lxml')
        list_con_li = bs.find('ul', class_="list_con_li")
        cartoon_list = list_con_li.find_all('a')
        for cartoon in cartoon_list:
            self.chapter_names.insert(0, cartoon.text)
            self.chapter_urls.insert(0, cartoon.get('href'))

    # 下载漫画
    def download(self):
        for i, url in enumerate(tqdm(self.chapter_urls)):
            download_header = {'Referer': url}
            name = self.chapter_names[i]
            # 去掉.
            while '.' in name:
                name = name.replace('.', '')
            chapter_save_dir = os.path.join(self.save_path, name)
            down_comic().create_dir(chapter_save_dir)  # 创建目录
            r = requests.get(url=url)
            html = BeautifulSoup(r.text, 'lxml')
            script_info = html.script
            pics = re.findall('\d{13,14}', str(script_info))
            for j, pic in enumerate(pics):
                if len(pic) == 13:
                    pics[j] = pic + '0'
            pics = sorted(pics, key=lambda x: int(x))
            chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]
            chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]
            for idx, pic in enumerate(pics):
                if pic[-1] == '0':
                    url = self.base_down_url + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
                else:
                    url = self.base_down_url + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
                pic_name = '%03d.jpg' % (idx + 1)
                pic_save_path = os.path.join(chapter_save_dir, pic_name)
                with closing(requests.get(url, headers=download_header, stream=True)) as response:
                    chunk_size = 1024
                    # content_size = int(response.headers['content-length'])
                    # print("文件大小：%s M" % (content_size/chunk_size))
                    if response.status_code == 200:
                        with open(pic_save_path, "wb") as file:
                            for data in response.iter_content(chunk_size=chunk_size):
                                file.write(data)
                    else:
                        print('链接异常')
            time.sleep(10)


if __name__ == '__main__':
    obj = down_comic()
    print('获取漫画连接中:')
    obj.get_chapter()
    print('漫画下载中>>>')
    obj.download()
    print('下载完成')