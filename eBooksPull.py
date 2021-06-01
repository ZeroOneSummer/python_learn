from bs4 import BeautifulSoup
import requests, sys

"""
    下载小说
    2021-05-31 by Aurora
"""
class down_novel(object):

    # init函数
    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/1_1094'
        self.chapters = []  #章节名称
        self.urls = []      #文章地址
        self.nums = []      #章节数

    # 获取目录&下载链接
    def get_text_url(self):
        req = requests.get(self.target)
        # req.encoding = req.apparent_encoding
        htmlText = req.text
        html = BeautifulSoup(htmlText, 'lxml')
        _directorys = html.find_all('div', class_='listmain')
        a_html = BeautifulSoup(str(_directorys), 'lxml')
        aList = a_html.find_all('a')
        newList = aList[12:]
        self.nums = len(newList)     # 剔除不必要的章节，并统计章节数
        for item in newList:
            self.chapters.append(item.string)
            down_url = self.target
            self.urls.append(down_url[0:down_url.rfind('/')] + item.get('href'))

    # 获取章节内容
    def get_contents(self, target):
        req = requests.get(target)
        htmlText = req.text
        html = BeautifulSoup(htmlText, 'lxml')
        texts = html.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    # 写入文件
    def writer(self, name, path, content):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as file:
            file.write(name + '\n')
            file.writelines(content)
            file.write('\n\n')

# 调用main
if __name__ == "__main__":
    obj = down_novel()
    obj.get_text_url()
    print('《一年永恒》开始下载>>>')
    for i in range(obj.nums):
        obj.writer(obj.chapters[i], '一念永恒.txt', obj.get_contents(obj.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / obj.nums) + '\r')   # %.3f小数点三位，%%百分号
        sys.stdout.flush()
    print('下载完成')
