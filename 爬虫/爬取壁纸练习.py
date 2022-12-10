"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re
"""

import requests
import re
import time

# <img src="https://desk-fd.zol-img.com.cn/t_s1366x768c5/g7/M00/0F/0B/ChMkLGJCtdiIP21SABwHM7LpzmwAAB-zgNMNp8AHAdL446.jpg">
# 下载页规律


# 请求头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
headers = {
    "User-Agent": user_agent
}


# 发送ruquests请求，拿到页面源代码
def set_requests(url, headers):
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'gb2312'
    pages = resp.text
    resp.close()
    return pages


# 解析网页，拿到下载地址
def parse_page(pages):
    obj = re.compile(
        # r'<div class="childclasslist_title.*?<div class="childclasslist_time">.*?<a href=".*?/std/(?P<url_id>.*?).html" target="_blank">(?P<name>.*?)</a>',
        r'<img src="(?P<data_url>.*?)">',
        re.S)
    # 开始匹配
    data_url = obj.findall(pages)
    return data_url


# 写入文件
def write_to_file(name, data):
    with open(name, 'wb') as f:
        f.write(data)
    print(name, "下载完成")


for n in range(100, 200):
    download_url = f"https://desk.zol.com.cn/showpic/1366x768_118{n}_377.html"
    pages = set_requests(download_url, headers)
    data_url = parse_page(pages)
    data = requests.get(data_url[0], headers).content
    write_to_file(f'./image/{n}.jpg', data)
    time.sleep(0.5)
