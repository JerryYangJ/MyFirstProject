'''
@author: JerryYang
@file: openai改造01.py
@time: 2023/1/26 21:14
@desc: 对openai-demo进行改造，将发送德问题改为用户输入德问题
'''

import openai

openai.api_key = '**************************88'  
ques = input("请输入你要问的问题：")
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Q:{ques}？\nA:",
    temperature=0,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
# print(type(response.get('choices')))
# print(type(response.get('choices')[0]))
print(response.get('choices')[0].get('text'))

'''
运行输出：
D:\pythonProject\pythonProject\openai\Scripts\python.exe D:/pythonProject/pythonProject/openai-demo.py
<class 'list'>
<class 'openai.openai_object.OpenAIObject'>
明天中国广东佛山的天气预报是晴转多云，最高气温30℃，最低气温22℃，风力3-4级。

Process finished with exit code 0
'''

'''
# 参数
  model:使用的模型："code-davinci-002"/"text-davinci-003"
  prompt: 生成提示，每个model的提示语不一样，需要注意
  temperature：创新采样，让结果更新颖，就调大值。
  top_p：情绪采样
  frequency_penalty：频率处罚系数
  presence_penalty：重复处罚系数
  stop:停止词

'''
