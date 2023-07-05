"""
@author: JerryYang
@file: openai改造01.py
@time: 2023/2/6 15:00
@desc: 增加功能：将返回德数据使用pyttsx3模块转换为语音
"""

import pyttsx3
import openai

openai.api_key = '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'  # openai api-keys : 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

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
print(response)
# resp_text = response.get('choices')[0].get('text')
resp_text = response.choices[0].text
# print(type(response.get('choices')))
# print(type(response.get('choices')[0]))
print("问：", ques)
print("AI回答内容:", resp_text)

# resp_text = '明天中国广东佛山的天气预报是晴转多云，最高气温30℃，最低气温22℃，风力3-4级。'

# 初始化tts引擎
engine = pyttsx3.init()

# 获取voices列表
voices = engine.getProperty('voices')
# 循环用不同voices播报
for voice in voices:
    # 设置发音人声音
    engine.setProperty('voice', voice.id)
    print(voice.id)
    # 调用引擎say()方法,开始朗读
    engine.say(resp_text)

# 等待语音播放完成
engine.runAndWait()

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
'''
语速控制
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

音量控制
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
'''
请输入你要问的问题：以下是某公司四个工厂产品制造检验合格率，请分析其中的问题：8010：86.1%、8020：99.1%、8030：94.4%、8040：93.0%、8050：87.3%

从上述数据可以看出，8020工厂的产品检验合格率最高，达到99.1%，而8050工厂的产品检验合格率最低，只有87.3%，这表明8050工厂的产品质量控制存在问题，需要加强管理和改进技术。
'''