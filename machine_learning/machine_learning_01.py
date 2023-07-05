"""
@author: JerryYang
@file: machine_learning_01.py
@time: 2023/4/9 10:44
@desc: 文字特征抽取（词云），字典特征抽取（one-hot)
"""

# # 文字特征抽取
# from sklearn.feature_extraction.text import CountVectorizer
# vector = CountVectorizer()
# res = vector.fit_transform(['lift is short, i love python', 'lift is too long, i hate python'])
# # toarray()可以将sparse矩阵转化为数组
# print(res.toarray())

import jieba
from sklearn.feature_extraction.text import CountVectorizer
text = [
    '然后，该系统利用多种机器学习技术进行自我培训，以便以一种近乎即时的方式对众多短文或答案进行自动评分。',
    '实际统计动物数量的艰巨任务是通过机器学习算法完成的。'
]
new_text = []
for t in text:
    r = list(jieba.cut(t))
    s = ' '.join(r)
    new_text.append(s)
c = CountVectorizer()
transform = c.fit_transform(new_text)
names = c.get_feature_names_out()
print(names)
print(transform.toarray())

# # 字典特征抽取
# # from sklearn.feature_extraction import DictVectorizer
# #
# # alist = [
# #     {'city': 'BeiJing', 'temp': 33},
# #     {'city': 'GZ', 'temp': 42},
# #     {'city': 'SH', 'temp': 40}
# # ]
# # # 创建工具对象
# # d = DictVectorizer(sparse=False)  # sparse=True 返回的是一个sparse矩阵; sparse=False 返回的是一个数组
# # # 使用工具对象进行特征值化
# # result = d.fit_transform(alist)
# # # 获取特征名称
# # names = d.get_feature_names_out()
# # print(names)
# # print(result)



