"""
@author: JerryYang
@file: 黑豹2.py
@time: 2023/5/30 21:47
@desc: Ok
        修改m3u8_file_path、save_path,并按实际情况是否需要增加base_url
"""
import os
import time
from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}


def down_ts(ts_line, ts_name, save_path):
    """
    下载ts文件
    :param ts_line: ts地址
    :param ts_name: 保存的ts文件名
    :return:
    """
    # 写文件前判断文件存储路径是否存在，不存在则创建路径

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

def decode_ts(ts_data, key):
    """
    :param ts_data: ts文件
    :param key: 解密用的key
    :return: 解密后的data
    """
    crypto = AES.new(key, AES.MODE_CBC, key)
    data = crypto.decrypt(ts_data)
    return data


if __name__ == '__main__':
    m3u8_file_path = 'D:\下载\汪汪队立大功之超能救援 .m3u8'
    save_path = './movie/汪汪队立大功之超能救援/'
    # 如果m3u8文件中的地址不是全地址，需要加上以下地址前缀，并启用第64行代码。
    base_url = f'https://ikcdn01.ikzybf.com/20221222/ne0BY6K1/2000kb/hls/'

    with ThreadPoolExecutor(8) as t:
        # 读取m3u8文件，下载ts
        with open(m3u8_file_path, 'r') as f:
            n = 1
            for ts_line in f:
                ts_line = ts_line.strip()
                if not ts_line.startswith("#"):
                    # ts_line = base_url+ts_line
                    # print(ts_line)
                    t.submit(down_ts, ts_line, n, save_path)
                    print(ts_line, n, "已提交")
                    n += 1
