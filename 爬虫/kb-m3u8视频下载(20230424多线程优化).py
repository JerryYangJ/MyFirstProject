"""
@author: JerryYang
@file: kb-m3u8视频下载(20230424多线程优化).py.py
@time: 2023/4/24 10:24
@desc:
"""
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"

}

episode = ''
url = f'https://www.bei-fa.com/vodplay/36867-1-{episode}.html'


def get_m3u8():
    """ 获取每集的m3u8文件 """
    # 向每集地址发送请求，获取源代码，提取m3u8请求地址
    for episode in range(1, 2):
        m3u8_index_rep = requests.get(url=url, headers=headers)
        print(m3u8_index_rep.text)
        m3u8_re = re.compile(f'"url":"(.*?)"')
        m3u8_index = m3u8_re.findall(m3u8_index_rep.text)
        print(m3u8_index)


def load_m3u8_file(episode):
    print(f"正在载入第{episode}集m3u8文件")
    ts_line_list = []
    m3u8_file_path = f"./movie/m3u8/{episode}.m3u8"

    with open(m3u8_file_path, 'r') as f:
        for ts_line in f:
            ts_line = ts_line.strip()
            if not ts_line.startswith("#"):
                ts_line_list.append(ts_line)
    return ts_line_list


def down_ts(ts_line, save_path, ts_name):
    # 向视频片段下载链接发送请求，获取数据。
    try:
        ts_resp = requests.get(url=ts_line, headers=headers)
        save_file(ts_resp, save_path, ts_name)
    except:
        print(ts_line, ts_name, "未成功下载")
        try:
            print(f"正在重试第{ts_name}：", ts_line, ts_name)
            ts_resp = requests.get(url=ts_line, headers=headers)
            save_file(ts_resp, save_path, ts_name)
        except:
            print(f"重试第{ts_name}失败，请手工下载：", ts_line)


def save_file(resp, save_path, ts_name):
    if resp.status_code == 200:
        with open(f'{save_path}/{ts_name}.ts', mode='wb') as f2:
            f2.write(resp.content)
        resp.close()
        print(f'{ts_name}完成下载', ts_line)


if __name__ == '__main__':
    with ThreadPoolExecutor(8) as t:
        # 读取m3u8文件，下载ts
        for episode in range(26, 30):
            # 写文件前判断文件存储路径是否存在，不存在则创建路径
            save_path = f'./movie/{episode}/'
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            ts_line_list = load_m3u8_file(episode)
            for i, ts_line in enumerate(ts_line_list):
                t.submit(down_ts, ts_line, save_path, i)
                print(ts_line, i, "已提交")
            print(f"第{episode}集下载提交完成")
    print("所有集数下载完成")

    # 下载完成后，用ffmpeg合并ts文件
    # os.system(f'ffmpeg -f concat -safe 0 -i D:/pythonProject/爬虫/movie/ts.txt -c copy D:\pythonProject\爬虫\movie\TS Merger tools\Merger\5.mp4')