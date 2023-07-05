"""
@author: JerryYang
@file: 猿人学JS逆向第13题.py
@time: 2023/5/27 15:35
@desc: ok
"""
import requests
import execjs

page=''
url1 = 'https://match.yuanrenxue.cn/match/13'
url = f'https://match.yuanrenxue.cn/api/match/13?page={page}'

sessionid = f'sessionid=w435146g2grsmcxpubz7ag3wpga5yjkz'
headers = {
    'User-Agent': 'yuanrenxue.project',
    'cookie': sessionid
}

# 请求url1,拿到返回的包含JS代码的响应数据
session_resp = requests.get(url=url1, headers=headers)

# 处理响应数据，得到cookie
js_code = session_resp.text.replace('<script>document.cookie=', '').replace(
    ';location.href=location.pathname+location.search</script>', '')
cookie_yuanrenxue = js_code.replace("(", '').replace(")", '').replace('+', '').replace("'", '')
# cookie_yuanrenxue = execjs.eval(js_code)
print(cookie_yuanrenxue)

# 拼接cookie
cookie = sessionid+';'+cookie_yuanrenxue
print(cookie)


headers1 = {
    'User-Agent': 'yuanrenxue.project',
    'Cookie': cookie
}

add_list = []
for page in range(1, 6):
    url = f'https://match.yuanrenxue.cn/api/match/13?page={page}'
    # 4.发送请求拿到数据
    resp = requests.get(url=url, headers=headers1)
    print(resp.text)
    resp = resp.json()
    value_list = resp['data']
    for value in value_list:
        # print(value.get('value'))
        add_list.append(value.get('value'))
print(add_list)
print(sum(add_list))

