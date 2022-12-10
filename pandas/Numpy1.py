import numpy as np

list=range(6)
#生成可迭代对象i
i=iter(list)
#使用i迭代器，通过fromiter方法创建ndarray
array=np.fromiter(i, dtype=float)
print(array)