'''
@author: JerryYang
@file: openai测试.py
@time: 2023/2/23 13:50
@desc: 优化：response的文本提取方式。
        新增功能：增加携带上下文持续对话功能
'''
from openai import Completion

# 使用GPT-2模型来创建一个文本自动完成模型
completion = Completion.create(engine="gpt2")

# 设置需要完成的文本，即用户需要输入的文本
prompt = "This is an example of OpenAI"

# 调用complete()函数完成文本
response = completion.complete(prompt, max_tokens=4)

# 打印结果
print(response)
