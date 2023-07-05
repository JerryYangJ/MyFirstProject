"""
    @ 正则表达式练习
"""

import re

str1 = '1cr,2cor,3coor, 4cooor, 5coooor, 6cooooor, 7coooooor, 8coooooooor'
pattern1 = r'co?r'
pattern2 = r'co+r'
pattern3 = r'co*r'
pattern4 = r'co{3}r'
pattern5 = r'co{3,}r'
pattern6 = r'co{3,4}r'
result = re.findall(pattern1, str1)
result2 = re.findall(pattern2, str1)
result3 = re.findall(pattern3, str1)
result4 = re.findall(pattern4, str1)
result5 = re.findall(pattern5, str1)
result6 = re.findall(pattern6, str1)
print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
