import requests, re, os, uuid, urllib3
from tqdm import tqdm

"""
    VIP视频解析
    2021-05-31 by Aurora
"""
if __name__ == "__main__":
    _header = {"Referer": "https://jx.618g.com/", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    _target_url = "https://v.qq.com/x/cover/mzc002001q141h4.html"
    _m3u8_base_v3 = "https://vod3.buycar5.cn"
    _m3u8_base_v4 = "https://vod4.buycar5.cn"
    _save_path = "C:\\Users\\v_pijiang\\Desktop\\ts\\"

    # 视频源
    _video_1 = "/20210506/M14Bx6z9/index.m3u8"
    _video_2 = "/20210106/WzKFGjOO/index.m3u8"

    # 获取ts列表
    _m3u8_p1 = requests.get(_m3u8_base_v4 + _video_2, headers=_header).text
    _m3u8_index = _m3u8_base_v4 + _m3u8_p1[_m3u8_p1.index("/"):].strip()
    urllib3.disable_warnings()
    _m3u8_file_list = requests.get(_m3u8_index)
    _ts_list = re.findall(r"^https:.*.ts$", _m3u8_file_list.text, re.M)

    # # 创建目录
    if not os.path.exists(_save_path):
        os.makedirs(_save_path)

    # 下载ts视频文件
    for ts_url in tqdm(_ts_list):
        with open(_save_path + str(uuid.uuid1()) + ".ts", "wb") as fp:
            ret = requests.get(ts_url, verify=False)
            fp.write(ret.content)

    # 合并成mp4
    os.system(r'copy /b ' + _save_path + '*.ts ' + _save_path + '三国无双.mp4')
    print("视频文件合并完成")





