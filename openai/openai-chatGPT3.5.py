"""
@author: JerryYang
@file: openai-chatGPT3.5.py
@time: 2023/3/7 8:15
@desc: openai-chatGPT3.5 模型调用
        测试已通过，需要梯子才能正常运行
"""

"""
官方接口调用Example：
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
"""

import pyttsx3
import openai
# openai.Model.list()

url = 'https://api.gpt-3.5-turbo.com/v1'
openai.api_key = '**************************' 

context = ''
while True:
    ques = input("问：")
    ques = ques + context
    print(ques)
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个制造业工厂质量管理专家"},
            {"role": "user", "content": ques}
        ]
    )
    context = resp['choices'][0]["message"]["content"]
    # print(resp)
    print("AI回答:", context)

# headers = {
#     'ContentType': 'application/json',
#     'Authorization': 'Bearer' + openai.api_key
# }

