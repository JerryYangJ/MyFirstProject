"""
@author: JerryYang
@file: 10.py
@time: 2023/6/13 21:51
@desc:
"""

import os, time, requests
url='https://sf9-dycdn-tos.pstatp.com/obj/tos-cn-i-8gu37r9deh/9d80ec60aef34dbd9ee8f893b85c58f7?filename=1.mp4'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"

}

def down_ts(ts_line, ts_name):
    '''
    下载ts文件
    :param ts_line: ts地址
    :param ts_name: 保存的ts文件名
    :return:
    '''
    # 写文件前判断文件存储路径是否存在，不存在则创建路径
    save_path = f'./movie/速度与激情10/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        time.sleep(1)
    # 向视频片段下载链接发送请求，获取数据。
    try:
        ts_resp = requests.get(url=ts_line, headers=headers)
        print(ts_resp.text)
        # with open(f'{save_path}/{ts_name}.mp4', mode='wb') as f2:
        #     f2.write(ts_resp.content)
        # ts_resp.close()
        # print(f'{ts_name}完成下载', ts_line)
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
    down_ts(url,"速度与激情1")