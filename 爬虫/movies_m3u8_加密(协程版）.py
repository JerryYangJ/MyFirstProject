"""
@author: JerryYang
@file: moviess_m3u8_加密（协程版）.py
@time: 2023/6/25 21:20
@desc: 注意：设置最大并发数避免Server Disconnected

"""
import os
import time
from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
import requests
import asyncio
import aiohttp
import aiofiles
import traceback


def decode_ts(data_list, key):
    """
    :param ts_data: ts文件
    :param key: 解密用的key
    :return: 解密后的data
    """
    de_data_list = []
    crypto = AES.new(key, AES.MODE_CBC, key)
    for d in data_list:
        data = crypto.decrypt(d)
        de_data_list.append(data)
    print("完成解密")
    return de_data_list


async def down_ts(ts_line, ts_name, headers, save_path, session):
    """
    下载ts文件
    :param ts_line: ts地址
    :param ts_name: ts文件名
    :return: 数据和名字
    """
    # 向视频片段下载链接发送请求，获取数据。
    try:
        async with session.get(url=ts_line, headers=headers) as ts_resp:
            async with aiofiles.open(f'{save_path}/{ts_name}.ts', 'wb') as f:
                await f.write(await ts_resp.content.read())
                print(f'{ts_name}完成下载')
    except Exception as e:
        # async with session.get(url=ts_line, headers=headers, timeout=30) as ts_resp:
        #     async with aiofiles.open(f'{save_path}/{ts_name}.ts', 'wb') as f:
        #         await f.write(await ts_resp.content.read())
        #         print(f'{ts_name}完成下载')
        traceback.print_exc()
        # print(ts_name, '\n', ts_line)

async def main():
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
    }
    # 读取m3u8文件路径
    m3u8_file_path = 'D:\下载\汪汪队立大功之超能救援.m3u8'
    # 保存路径
    save_path = './movie/汪汪队立大功之超能救援(协程)/'
    # 保存文件前判断文件存储路径是否存在，不存在则创建路径
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        time.sleep(1)
    # # 如果m3u8文件中的地址不是全地址，需要加上以下地址前缀，并启用第87行代码。
    # base_url = f'https://s2.fsvod1.com'
    # # 获取key的地址
    # key_url = 'https://s2.fsvod1.com/20220330/fZ217AvW/1200kb/hls/key.key'
    # # 获取key
    # key = requests.get(key_url, headers=headers)
    # # print(key.text)
    # key = key.content

    tasks = []
    # data_list = []

    # 将超时时间设置为600秒
    timeout = aiohttp.ClientTimeout(total=600)
    # 并发数量设置为10(设置过大容易出现Server Disconnected错误
    connector = aiohttp.TCPConnector(limit=10)
    # 创建一个异步session
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # 读取m3u8文件，提取url，创建协程对象
        with open(m3u8_file_path, 'r') as f:
            n = 1
            for ts_line in f:
                ts_line = ts_line.strip()
                if not ts_line.startswith("#"):
                    # ts_line = base_url + ts_line
                    print(f'{n}:{ts_line}')
                    task = asyncio.create_task(down_ts(ts_line, n, headers, save_path, session))
                    tasks.append(task)
                    n += 1
        # 启动协程对象
        await asyncio.gather(*tasks)
    print("Download completd!!")
    # # 获取下载的数据
    # for future in future_list:
    #     data = future.result()[0]
    #     data_list.append(data)
    # # # 解密数据
    # # decode_data_list = decode_ts(data_list, key)
    # # # 合并保存数据
    # # merge_ts_files(decode_data_list, save_path)


# 向视频片段下载链接发送请求，获取数据。


# def save_data(data, name, save_path):
#     with open(f'{save_path}/{name}.ts', mode='wb') as f2:
#         f2.write(data)
#     print(f'{name}完成下载')

#
# def merge_ts_files(data, save_path):
#     '''
#     合并ts文件
#     :param output_file: 合并后的文件名
#     :param ts_files: 需要合并的TS文件列表
#     :param save_path: 保存文件路径
#     :return:
#     '''
#     output_file = save_path.split('/')[-2] + '.mp4'  # 合并后的TS文件名
#     with open(save_path + output_file, 'wb') as outfile:
#         for ts_data in data:
#             outfile.write(ts_data)
#     print("完成合并，保存路径", save_path+output_file)


if __name__ == '__main__':
    asyncio.run(main())

