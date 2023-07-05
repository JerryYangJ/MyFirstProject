"""
@author: JerryYang
@file: 猿人学JS逆向第3题.py
@time: 2023/5/29 10:32
@desc: ok,此题服务器会对headers顺序进行验证，requests会自动对headers顺序进行排序，无法通过验证。需要适用session来保持headers的顺序
"""
import time

import requests
from collections import defaultdict

sessionid = 'sessionid=x8ebi94vj52mafor340wcbey8shzv8tf'
url = 'https://match.yuanrenxue.cn/match/3'
api_url = 'https://match.yuanrenxue.cn/api/match/3?page=1'
set_cookie_url = 'https://match.yuanrenxue.cn/jssm'  # post

session = requests.session()
# 设置headers（必需同服务器验证顺序一样）
headers = {
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://match.yuanrenxue.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'yuanrenxue.project',
}

# 设置cookies
cookies = {
    "sessionid": 'x8ebi94vj52mafor340wcbey8shzv8tf',
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1680358730,1680422054,1680422750,1680533041",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "7117510294618647776",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1680229861,1680334932,1680424481,1680533049",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1680533049",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1680533051"
}

# 初始化数据
add_list = []
temp = 0
max_id = ''

# 设置session的headers
session.headers = headers

# 获取每页的数据，加入到add_list列表中
for page in range(1, 6):
    # 通过session访问set_cookie页面，拿到cookie
    resp = session.post(url=set_cookie_url, cookies=cookies)
    print(resp.cookies)

    # 带着cookies访问目标数据页，获取数据
    url = f'https://match.yuanrenxue.cn/api/match/3?page={page}'
    resp = session.get(url=url, cookies=cookies)
    print(resp.text)

    # 处理数据
    resp = resp.json()
    value_list = resp['data']
    for value in value_list:
        # print(value.get('value'))
        add_list.append(value.get('value'))
print(add_list)

# 对数据列表add_list进行遍历，找出重复最多的元素及其值
for data in add_list:
    if(add_list.count(data)) > temp:
        temp = add_list.count(data)
        max_id = data
print(f'{max_id}出现的最多，出现了{temp}次')



