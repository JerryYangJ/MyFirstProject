"""
@author: JerryYang
@file: 自动创建文件夹.py
@time: 2023/3/25 18:06
@desc: 判断文件夹是否存在，如不存在，则自动创建
"""

import os

# 文件保存路径
save_path = f'./我是自动创建的文件夹'
# 方法1：
if not os.path.exists(save_path):
    os.mkdir(save_path)



# # 判断保存文件的文件夹（路径）是否存在
# if os.path.exists(save_path):
#     print(save_path, "存在")
# else:
#     print(save_path, "不存在")
#     # 自动创建
#     os.mkdir(save_path)
#     print(save_path, "已自动创建")


