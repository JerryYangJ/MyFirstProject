import re

'''
实战演练：从下面的 HTML 代码中使用 re 模块提取出两部影片的名称和主演信息。
'''
html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""

# 正则表达式
data = re.compile(r'<div.*?<a title=.*?>(.*?)</a.*?<p class="star">.*?主演：(.*?)</p.*?div>', re.S)
# data = re.compile(r'<div.*?<a title="(.*?)".*?"star">(.*?)</p.*?div>', re.S)
result_list = data.findall(html)
print(result_list)

for info in  result_list:
    print('电影名称：', info[0])
    print('主演：', info[1].strip())
