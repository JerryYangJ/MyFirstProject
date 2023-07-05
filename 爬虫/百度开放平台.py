'''
@author: JerryYang
@file: 百度开放平台.py
@time: 2023/2/15 13:51
@desc:
'''

# 申请信息
'''

APP ID：20221003001368520
密钥：nA15Jn0vBAnkuNShHami
'''
# 语音翻译API接入
'''
接口限制：
需要上传完整的录音文件，录音文件时长不超过 60 秒
音频编码要求：采样率 16000、8000，16 bit 位深，单声道
支持音频语种及格式：

语种	格式
中文、粤语	pcm、wav、amr、m4a
英语、日语、韩语、俄语、德语、法语、泰语、葡萄牙语、西班牙语、阿拉伯语	pcm

音频格式说明：
pcm（无损音频格式）：也称为 raw 格式。音频输入最原始的格式，不用解码。
wav（无损音频格式，pcm 编码）：在 pcm 格式的开头额外包含一段描述采样率、编码等信息的编码。
amr（有损压缩格式）：对音频数据进行有损压缩，类似 mp3 文件。
m4a（有损压缩格式，AAC 编码）：对音频数据进行有损压缩，通常仅供微信小程序使用的格式。

接入方式：
语音翻译API HTTPS地址：https://fanyi-api.baidu.com/api/trans/v2/voicetrans
请求方式： POST
'''
# 请求参数
'''
Headers

参数名称	示例	是否必填	备注
Content-Type	application/json	是	
X-Appid	appid	是	APPID 从管理控制台中获得
X-Timestamp	1642331332	是	Unix时间戳（10位）
X-Sign	i1b/6Ml/NxhEhOnsiQIK7nqsPH/avhhlHgfpo84lJC8=	是	请求签名。请参考 请求签名计算方法 小节

Body

参数名	参数类型	是否必填	示例	备注
from	string	是	en	源语言的语言代码，具体参考语种列表
to	string	是	zh	目标语言的语言代码，具体考语种列表
voice	string	是	W3NvdXJjZSBhdWRpbyBieXRlc10K	语音文件二进制数据，base64编码
format	string	是	pcm	音频文件格式。请参考语言列表和音频格式。需上传完整的音频数据，包含的音频时长不超过 60 秒，并且数据大小不超过4MB（base64编码前）

示例
{
"from": "en",
"to": "zh",
"format":"pcm",
"voice": "W3NvdXJjZSBhdWRpbyBieXRlc10K"
}
'''
# 响应参数
'''
Header

参数名称	参数类型	示例	备注
X-MT-Logid	string	970e51a03f5c42ba8868bdad786c13d8	返回唯一logid

Body

参数名称	参数类型	示例	备注
code	int	0	错误码
0：成功
非0：失败
msg	string	Success	错误信息
data	object		结果结构，当且仅当code为 0 时存在
data.source	string	今天天气不错。	语音识别的原文
data.target	string	It's a nice day today.	翻译后的译文
data.target_tts	string	W2F1ZGlvIGJ5dGVzXQo=	译文 TTS，base64数据
正常情况
{
"code": 0,
"msg": "Success",
"data": {
"source": "今天天气不错。",  // 识别原文
"target": "It's a nice day today.",  // 译文
"target_tts": "W2F1ZGlvIGJ5dGVzXQo="  // 译文TTS ，base64编码
}
}
'''
# 请求签名 X-Sign 计算方法
'''
将音频文件进行base64编码，得到音频编码 ，即用于请求参数中的 voice 字段
拼接字符串： X-Appid +  X-Timestamp + voice  
使用 hmac_sha256 加密算法对（2）中的字符串进行加密，并得到base64格式的签名（因为hmac一般得到的是二进制字节流），做为 X-Sign 。hmac_sha256 的密钥来自于使用翻译开放平台分配的密钥，（可在 管理控制台 - 开发者信息获得）

示例
appid = '2015063000000001'  # 请替换为您的APP ID
timestamp = '1646034877'  # 10位Unix时间戳
voice_bytes = b'00010101011101010101'
secret_key = 'XWG7Gyj'  # 翻译开放平台分配的密钥
# step1: base64编码音频文件
voice = base64encode(voice_bytes)
# step2: 得到待加密的字符串
msg = appid + timestamp + voice
# step3: 加密得到签名，作为`X-Sign`。若hmac得到的是二进制字节，需要进行base64编码
sign = base64encode(hmac_sha256(secret=secret_key, message=msg))
'''

import requests

appid = '20221003001368520'
url = 'https://fanyi-api.baidu.com/api/trans/v2/voicetrans'
headers = {
    'Content-Type': 'application/json',
    'X-Appid': appid,
    'X-Timestamp': '1642331332',
    'X-Sign': 'i1b/6Ml/NxhEhOnsiQIK7nqsPH/avhhlHgfpo84lJC8='

}

data = {
    "from": "en",
    "to": "zh",
    "format": "pcm",
    "voice": "W3NvdXJjZSBhdWRpbyBieXRlc10K"
}

resp = requests.post(url=url, headers=headers, data=data)
print(resp.text.encode().decode("unicode_escape"))
