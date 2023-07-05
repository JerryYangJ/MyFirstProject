"""
@author: JerryYang
@file: 猿人学JS逆向第1题.py.py
@time: 2023/6/5 10:34
@desc: OK。混淆JS，主要是计算请求地址的加密参数m
"""
import time

import requests
import execjs
from statistics import mean

page = ''
m = ''
sessionid = f'sessionid=0vwj6u2hh1z7amytvxj0nju4fpdg3976'

headers = {
    'User-Agent': 'yuanrenxue.project',
    'cookie': sessionid
}

add_list = []
for page in range(1, 6):
    # 处理加密参数m
    with open(r'./猿人学JS逆向第一题JS_md5.js', 'r', encoding="utf-8") as f:  # /baidufanyi.js表示js文件
        jscode = f.read()
    js_obj = execjs.compile(jscode)  # 编译js文件
    # 获取时间戳
    datatime = int(time.time()) * 1000 + 100000000
    mm = str(int(datatime / 1000))
    print(int(datatime), mm)
    m = js_obj.call('hex_md5', str(int(datatime)))  # hex_md5表示要调用的js函数,datatime表示传的参数
    m = m + '丨' + mm
    print(m)
    url = f'https://match.yuanrenxue.cn/api/match/1?page={page}&m={m}'
    print(url)
    # 4.发送请求拿到数据
    resp = requests.get(url=url, headers=headers)
    print(resp.text)
    resp = resp.json()
    value_list = resp['data']
    for value in value_list:
        # print(value.get('value'))
        add_list.append(value.get('value'))
print(add_list)

# 统计平均值：mean函数
# print(sum(add_list)/len(add_list))
print(mean(add_list))


# https://match.yuanrenxue.cn/api/match/1?page=2&m=152e6f0b91bd35521b3276b88e0af90c|1686032634
# https://match.yuanrenxue.cn/api/match/1?page=1&m=fc3008e9d6acf8c08009df72a757ee83|1686034471