import os
import openai

openai.api_key = '****************88'  

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="# Python 3 \ndef remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn x \n\n# Explanation of what the code does\n\n#",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)



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
