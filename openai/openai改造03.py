"""
@author: JerryYang
@file: openai改造01.py
@time: 2023/2/7 9:50
@desc: 优化：response的文本提取方式。
        新增功能：增加携带上下文持续对话功能
"""

import pyttsx3
import openai

openai.api_key = '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'  # openai api-keys : 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

context = ''
while True:
    ques = input("问：")
    ques += context
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
    print("AI回答:", resp_text)


    # # 初始化tts引擎
    # engine = pyttsx3.init()
    #
    # # 获取voices列表
    # voices = engine.getProperty('voices')
    # # 循环用不同voices播报
    # for voice in voices:
    #     # 设置发音人声音
    #     engine.setProperty('voice', voice.id)
    #     # print(voice.id)
    #     # 调用引擎say()方法,开始朗读
    #     engine.say(resp_text)
    #
    # # 等待语音播放完成
    # engine.runAndWait()
    #
    # # 将以上对话内容加入到下次提问中（将上下文加入下次提问）
    # context += ques + "\n" + resp_text
    # # print("context:", context)



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
问：以下是某公司四个工厂产品制造检验合格率，请分析其中的问题：8010：86.1%、8020：99.1%、8030：94.4%、8040：93.0%、8050：87.3%
AI回答: 从上述数据可以看出，8020工厂的产品检验合格率最高，达到99.1%，而8050工厂的产品检验合格率最低，只有87.3%，这表明8050工厂的产品质量控制存在问题，需要加强管理和改进技术。

问：有没有可能性是部分工厂的数据有问题。一般来说同一个公司的制造和管理水平相当，制造过程的检验合格率差异一般不会太大的。
AI回答: 是的，有可能性是部分工厂的数据有问题。

问：还会有其他可能的原因么？
AI回答: 是的，有可能性是部分工厂的数据有问题。可能是由于检验标准不一致、检验过程不同、检验仪器不同等原因导致的。此外，还可能是由于生产工艺、原材料质量、设备维护等原因导致的。

问：有什么好的管理措施保证这些数据的准确性？
AI回答: 为了保证数据的准确性，可以采取以下管理措施：
1.统一检验标准：为了保证检验结果的准确性，需要统一检验标准，确保各个工厂的检验标准一致。
2.定期检查：定期对各个工厂的检验过程进行检查，确保检验过程的一致性。
3.定期维护：定期对检验仪器进行维护，确保检验仪器的准确性。
4.定期检查：定期对生产工艺、原材料质量、设备维护等进行检查，确保产品质量的稳定性。'''
