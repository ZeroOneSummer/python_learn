import urllib, urllib3, re, os

'''
    调用IDM下载
'''
if __name__ == "__main__":
    sava_path = 'C:\\Users\\v_pijiang\\Desktop\\excel_test\\'
    down_url = 'magnet:?xt=urn:btih:5f43da7921fd1d35e53b49b5e0ff72e5ec2f68ff&dn=[电影天堂www.dytt89.com]姜子牙HD国语中字.mp4'
    # bytes(down_url, encoding="utf8")
    print(down_url)
    # IDMPath = "D:\\install\\Internet Download Manager\\"
    # os.chdir(IDMPath)
    # IDM = "IDMan.exe"
    # command = ' '.join([IDM, '/d', down_url, '/p', sava_path, '/f', '姜子牙.mp4', '/a', '/s'])
    # os.system(command)
