# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :网站：http://www.akmeiju.cc/vplay/10367-1-6.html上电影《达芬奇恶魔》第一季下载
from concurrent.futures import ThreadPoolExecutor

import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

base_url = 'https://b3.szjal.cn'


# 1.向m3u8网址发送请求，获取m3u8文件

# 2.读取m3u8文件，提取下载链接。
def down_m3u8(m3u8_num):
    n = 1
    with open(f'./movie/达芬奇恶魔/{m3u8_num}.m3u8', 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith("#"):
                with ThreadPoolExecutor(50) as ts:
                    ts.submit(down_ts, m3u8_num, line, n)
                    n += 1


def down_ts(i, line, n):
    down_url = base_url + line
    # print(down_url)
    # 3.向视频片段下载链接发送请求，获取数据。
    resp = requests.get(url=down_url, headers=headers)
    # 4.存储数据
    f = open(f'./movie/达芬奇恶魔/{i}/{n}.ts', mode='wb')
    f.write(resp.content)
    print(f'{i}-{n}完成下载')
    n += 1


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in [2, ]:
            t.submit(down_m3u8, i)
# 5.合并数据
