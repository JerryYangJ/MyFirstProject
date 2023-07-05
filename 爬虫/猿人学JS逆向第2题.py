"""
@author: JerryYang
@file: 猿人学JS逆向第2题.py
@time: 2023/6/2 13:55
@desc: 1.每次访问match/2时cookies的m参数会变化，2.拿到m产生函数，带着m参数重新访问api/match/2即可拿到数据
"""
import requests
import base64

# 登录后获取自己的sessionid(每次登录会不一样)
sessionid = 'sessionid=jkgx4ne2pn9tr6vx9069h37tc2515ixq'

url = 'https://match.yuanrenxue.cn/match/2'
api_url = 'https://match.yuanrenxue.cn/api/match/2?page=1'

headers = {
    'User-Agent': 'yuanrenxue.project',
    'cookie': sessionid
}

rsp = requests.get(url=url, headers=headers)
print(rsp.text)
print(rsp.status_code)
print(rsp.cookies)




# # 1.定义所有数据的列表
# add_list = []
#
# for page in range(1, 4):
#     page = str(page)
#     # 数据接口url
#     url = f'https://match.yuanrenxue.cn/api/match/2?page={page}'
#
#     # 4.发送请求拿到数据（只拿前3页数据，第4、5页需要登录才能拿数据）
#     headers = {
#         'User-Agent': 'yuanrenxue.project',
#         'Cookie': sessionid
#     }
#     resp = requests.get(url=url, headers=headers)
#     print(resp.text)
#     resp= resp.json()
#     value_list = resp['data']
#     for value in value_list:
#         # print(value.get('value'))
#         add_list.append(value.get('value'))
# print(add_list)
# print(sum(add_list))