"""
@author: JerryYang
@file: openai-chatGPT3.5.py
@time: 2023/3/7 8:15
@desc: 另一种openai-chatGPT3.5 模型调用方法，直接使用requests模块调用接口
        测试未通过，测试需要梯子
"""

import requests

# GPT-3.5 Turbo API Endpoint
endpoint = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions'

# GPT-3.5 Turbo API Key
api_key = '*******************88'

# Sample GPT-3.5 Turbo Prompt
prompt = 'The meaning of life is '

# Prepare GPT-3.5 Turbo Request
request = {
    'prompt': prompt,
    'max_tokens': 5
}

# Execute Request
response = requests.post(
    endpoint,
    json=request,
    headers={'Authorization': 'Bearer ' + api_key}
)

# Print Result
print(response.json()['choices'][0]['text'])

# Output:
# to find happiness and contentment.
