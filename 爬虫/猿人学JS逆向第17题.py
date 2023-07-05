"""
@author: JerryYang
@file: 猿人学JS逆向第17题.py.py
@time: 2023/6/1 13:54
@desc: ok（采用http2协议，requests库无法兼容http2协议，需要适用httpx库
"""
import httpx


sessionid = f'sessionid=w435146g2grsmcxpubz7ag3wpga5yjkz'
headers = {
    'User-Agent': 'yuanrenxue.project',
    'cookie': sessionid
}

add_list = []
for page in range(1, 6):
    url = f'https://match.yuanrenxue.cn/api/match/17?page={page}'
    # 4.发送请求拿到数据
    with httpx.Client(headers=headers, http2=True) as client:
        resp = client.get(url)
        print(resp.text)
        resp = resp.json()
        value_list = resp['data']
        for value in value_list:
            # print(value.get('value'))
            add_list.append(value.get('value'))
print(add_list)
print(sum(add_list))
