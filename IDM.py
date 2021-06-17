import urllib, urllib3, re, os

'''
    调用IDM下载
'''
if __name__ == "__main__":
    sava_path = 'C:\\Users\\v_pijiang\\Desktop\\excel_test\\'
    down_url = 'ftp://a.gbl.114s.com:20320/5393/姜子牙-2020_HD国语中字.mp4'
    IDMPath = "D:\\install\\Internet Download Manager\\"
    os.chdir(IDMPath)
    IDM = "IDMan.exe"
    command = ' '.join([IDM, '/d', down_url, '/p', sava_path, '/f', '姜子牙.mp4', '/a', '/s'])
    os.system(command)
