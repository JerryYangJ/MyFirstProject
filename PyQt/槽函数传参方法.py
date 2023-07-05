"""
@author: JerryYang
@file: 槽函数传参方法.py
@time: 2023/4/21 20:48
@desc:
"""
'''
方法一：使用lambda表达式
button.clicked.connect(lambda:self.onButtonClick(1))

方法二：使用partial函数
button.clicked.connect(partial(self.onButtonClick,1))

'''

