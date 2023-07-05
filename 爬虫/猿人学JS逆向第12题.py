"""
@author: JerryYang
@file: 猿人学JS逆向第12题.py
@time: 2023/5/27 11:54
@desc: ok
"""
import requests
import base64

# 登录后获取自己的sessionid(每次登录会不一样)
sessionid = 'sessionid=kv3h9g1zart0ztzria2ozm9c7b1k0xpc'

# 1.定义所有数据的列表
add_list = []

for page in range(1, 6):
    page = str(page)
    # 2.将参数m转为Base64编码
    m = 'yuanrenxue' + page
    print(m)
    m = base64.b64encode(m.encode('utf-8')).decode()
    print(m)

    # 3.url地址
    url = f'https://match.yuanrenxue.cn/api/match/12?page={page}&m={m}'
    # url = 'https://match.yuanrenxue.cn/api/match/12' + '?' + 'page=' + page + '&' + 'm=' + m
    print(url)


    # 4.发送请求拿到数据
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie': sessionid
    }
    resp = requests.get(url=url, headers=headers)
    print(resp.text)
    resp = resp.json()
    value_list = resp['data']
    for value in value_list:
        # print(value.get('value'))
        add_list.append(value.get('value'))
print(add_list)
print(sum(add_list))