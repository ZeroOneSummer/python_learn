import requests
import json

# 获取网页信息
url = 'http://www.cntour.cn/'
response = requests.get(url)
print(response.text)

def get_transText(word=None):
    _url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    _from_data = {'i':word,'from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb',\
                  'salt':'16224413641783','sign':'81dafe2e8d0fb4ad163533184ab39894','lts':'1622441364178',\
                  'bv':'a755cd5c0dc961644e9813fce38588b3','doctype':'json','version':'2.1',\
                  'keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION'}
    _response = requests.post(_url, data=_from_data)
    _content = json.loads(_response.text)
    print(_content)
    # 打印翻译后的意思
    print(_content['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    get_transText('我爱中国')
