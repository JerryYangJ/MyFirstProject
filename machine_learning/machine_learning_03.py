"""
@author: JerryYang
@file: machine_learning_03.py
@time: 2023/4/9 12:16
@desc: 特征工程——归一化和标准化
        归一化：异常值对结果影响较大，往往数据中最大值和最小值的异常值比较大。
        标准化：异常值对结果影响较小。
"""


from sklearn.preprocessing import MinMaxScaler, StandardScaler
mm = MinMaxScaler(feature_range=(0, 1))
aa = StandardScaler()