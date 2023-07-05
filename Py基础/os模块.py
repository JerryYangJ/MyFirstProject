"""
@author: JerryYang
@file: os模块.py
@time: 2023/4/15 11:19
@desc: os模块的作用：可以处理文件和目录这些我们日常手动需要做的操作。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。
"""
import os

# os.name:输出字符串指示正在使用的平台。如果是window 则用'nt'表示，对于Linux/Unix用户，它是'posix'。
import time

print("使用的系统是：", os.name)

# os.getcwd():函数得到当前工作目录，即当前Python脚本工作的目录路径
print("脚本当期的工作目录是：", os.getcwd())

# os.listdir():返回指定目录下的所有文件和目录名。
print("当前目录下所有目录和文件：", os.listdir(os.getcwd()))

# # os.remove()：删除一个文件。
# with open('./a.txt', 'w', encoding='utf-8') as f:       # 在当前目录下创建一个a.txt文件
#     pass
# time.sleep(10)
# os.remove('./a.txt')   # 10秒后删除创建的文件

# # os.system():运行shell命令
# name = os.system('dir')
# print(name)

# os.sep:可以取代操作系统特定的路径分割符
print(os.sep)

# os.linesep:字符串给出当前平台使用的行终止符
print(os.linesep)

# os.path.split():函数返回一个路径的目录名和文件名。
print(os.path.split(os.getcwd()))
print(os.path.split("D:\pythonProject\py基础\os模块.py"))

# os.path.splitext():分离文件名与扩展名。
print(os.path.splitext("D:\pythonProject\py基础\os模块.py"))

# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))
print(os.path.isfile("D:\pythonProject\py基础\os模块.py"))
print(os.path.isdir("D:\pythonProject\py基础\os模块.py"))

# os.path.exists()函数用来检验给出的路径是否真地存在
print(os.path.exists("D:\pythonProject\py基础\os模块.py"))
print(os.path.exists("D:\pythonProject\py基础"))

# os.path.abspath(name):获得绝对路径
print(os.path.abspath("os模块.py"))

# os.path.normpath(path):规范path字符串形式
print(os.path.normpath("D:\pythonProject\py基础\os模块.py"))

# os.path.getsize(name):获得文件大小，如果name是目录返回0L。
print(os.path.getsize("D:\pythonProject\py基础\os模块.py"))

# os.path.join(path,name):连接目录与文件名或目录
print(os.path.join(os.getcwd(), 'aaa.txt'))

# os.path.basename(path):返回文件名
print(os.path.basename("D:\pythonProject\py基础\os模块.py"))

# os.path.dirname(path):返回文件路径。
print(os.path.dirname("D:\pythonProject\py基础\os模块.py"))
