# @Time :2022/11/30 8:34
# @Author : Jerry Y
# @File  : PyExecJS库用法.py
# @Info  :
import execjs

print(execjs.eval("'red yellow blue'.split(' ')"))

# 编译js
compile_code = execjs.compile(open('./baidufanyi.js', 'r', encoding='utf-8').read())

# 实用编译后的代码块call函数调用js文件中的hello_word函数
result = compile_code.call('f', '日本')
print(result)

