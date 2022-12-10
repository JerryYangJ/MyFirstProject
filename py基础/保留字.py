"""
    @保留字
    @定义：是被赋予特定意义的单词。不能作为变量、函数、类、模块和其他对象的名称来使用
    @区分大小写
"""

"""
 （['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']）

"""

# 可以使用以下代码查看保留字    不同版本保留字可能不一样？
import keyword
print(keyword.kwlist)
print("保留字总数为：",len(keyword.kwlist))

