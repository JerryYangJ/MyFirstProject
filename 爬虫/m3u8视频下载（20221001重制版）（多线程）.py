# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :
import os.path
import re
from concurrent.futures import ThreadPoolExecutor

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"

}


def down_ts(i, ts_line, ts_name):
    # 向视频片段下载链接发送请求，获取数据。
    ts_resp = requests.get(url=ts_line, headers=headers)
    # 4.存储数据
    with open(f'./movie/m3u8_1/{i}/{ts_name}.ts', mode='wb') as f2:
        f2.write(ts_resp.content)
    ts_resp.close()
    print(f'{i}-{ts_name}完成下载')


if __name__ == '__main__':
    m3u8_base = 'https://kankanb.35ju.com:1234/jxplayer.php?'
    ts_base_list = []
    all_task = []

    with ThreadPoolExecutor(10) as t:
        # 1.向每集的页面发送请求，获取v的值.获取m3u8文件的获取地址
        for i in range(0, 12):
            n = 1
            index_url = f'https://www.39xp.com/kb/78659-0-{i}.html'
            resp = requests.get(url=index_url, headers=headers)
            v_re = re.compile(f'var now="(.*?)"')
            v = v_re.findall(resp.text)[0]
            resp.close()
            # print(v)
            # m3u8页面地址
            m3u8_url = m3u8_base + v
            # print(m3u8_url)

            # 向m3u8文件获取地址页面发送请求，解析m3u8地址
            resp1 = requests.get(url=m3u8_url, headers=headers)
            m3u8_re = re.compile(f'var urls = "(.*?)"')
            m3u8_rel_url = m3u8_re.findall(resp1.text)[0]
            resp1.close()
            # print(m3u8_rel_url)
            ts_base = m3u8_rel_url.replace(f'RongXingVR.m3u8', '')
            # print(ts_base)
            ts_base_list.append(ts_base)

            # 2.向m3u8页面地址发送请求，下载m3u8文件
            resp2 = requests.get(url=m3u8_rel_url, headers=headers)
            # 写文件前先判断文件路径是否存在，不存在则创建路径
            save_path = f'/movie/m3u8'
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            with open(f'{save_path}/{i + 1}.m3u8', 'wb') as f:
                f.write(resp2.content)
            resp2.close()

            # 读取m3u8文件，下载ts
            with open(f'./movie/m3u8/{i + 1}.m3u8', 'r') as f1:
                for ts_line in f1:
                    ts_line = ts_line.strip()
                    if not ts_line.startswith("#"):
                        # 3.向视频片段下载链接发送请求，获取数据。
                        ts_line = ts_base_list[i] + ts_line
                        # print(f'第{i+1}集,第{n}个ts地址{ts_line}，准备下载')
                        t.submit(down_ts, i + 1, ts_line, n)
                        n += 1
    print("所有视频下载完成")
