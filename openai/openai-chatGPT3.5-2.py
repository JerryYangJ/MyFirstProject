"""
@author: JerryYang
@file: openai-chatGPT3.5-2.py
@time: 2023/3/10 22:20
@desc: 在v0版本上增加上下文功能
"""

import openai


url = 'https://api.gpt-3.5-turbo.com/v1'
openai.api_key = '*******************8'  

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个程序员"},
        {"role": "user", "content": "用python写一个gpt-3.5-turbo模型接口调用代码"}
    ]
)

# headers = {
#     'ContentType': 'application/json',
#     'Authorization': 'Bearer' + openai.api_key
# }

# print(resp)
print(resp['choices'][0]["message"]["content"])
