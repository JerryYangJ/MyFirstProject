"""
@author: JerryYang
@file: 黑豹2.py
@time: 2023/5/30 21:47
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
base_url = f'https://vip.lz-cdn4.com/20230131/25604_a87f167d/1800k/hls/'


def down_ts(ts_line, ts_name):
    # 写文件前判断文件存储路径是否存在，不存在则创建路径
    save_path = f'./movie/黑豹2/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        time.sleep(1)
    # 向视频片段下载链接发送请求，获取数据。
    try:
        ts_resp = requests.get(url=ts_line, headers=headers)
        with open(f'{save_path}/{ts_name}.ts', mode='wb') as f2:
            f2.write(ts_resp.content)
        ts_resp.close()
        print(f'{ts_name}完成下载', ts_line)
    except:
        print(ts_line, ts_name, "未成功下载")
        try:
            print(f"正在重试第{ts_name}：", ts_line, ts_name)
            ts_resp = requests.get(url=ts_line, headers=headers)
            with open(f'{save_path}/{ts_name}.ts', mode='wb') as f2:
                f2.write(ts_resp.content)
            ts_resp.close()
            print(f'{ts_name}完成下载', ts_line)
        except:
            print(f"重试第{ts_name}失败，请手工下载：", ts_line)


if __name__ == '__main__':
    with ThreadPoolExecutor(8) as t:
        # 读取m3u8文件，下载ts
        with open(f'D:\下载\mixed.m3u8', 'r') as f:
            n = 1
            for ts_line in f:
                ts_line = ts_line.strip()
                if not ts_line.startswith("#"):
                    ts_line = base_url+ts_line
                    # print(ts_line)
                    t.submit(down_ts, ts_line, n)
                    print(ts_line, n, "已提交")
                    n += 1
