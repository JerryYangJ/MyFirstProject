"""
@author: JerryYang
@file: dictation.py
@time: 2023/2/27 18:12
@desc:
"""
import time

import pyttsx3


def to_say(word):
    """文字转语音输出"""
    # 初始化tts引擎
    engine = pyttsx3.init()

    # 获取voices列表
    voices = engine.getProperty('voices')
    print(type(voices))

    for voice in voices:
        # 设置发音人声音
        engine.setProperty('voice', voice.id)
        # 调用引擎say()方法,开始朗读
        engine.say(word)

        time.sleep(2)
    engine.runAndWait()



def main():
    """ 主函数 """
    word_str = input("输入需要听写单词:")  # "Hello,\nMy name is John.\nNice to meet you."
    word_list = word_str.split(' ')
    for word in word_list:
        time.sleep(3)
        to_say(word)


if __name__ == '__main__':
    main()
