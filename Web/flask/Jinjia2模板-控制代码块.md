# 模板-控制代码块
控制代码块主要包含两个：
1.for循环
2.if判断


# 1. if语句
Jinja2模板引擎 语法中的if语句跟 Python 中的 if 语句相似, if 判断的结果是布尔值，将决定代码中的哪个流程会被执行:

```htm
{% if user.is_logged_flag %}
    <a href='/logout'>Logout</a>  <!-- 如果登录了，就应该显示 可以点击"退出" -->
{% else %}
    <a href='/login'>Login</a>
{% endif %}
```


过滤器可以被用在 if 语句中:

```htm
{% if comments | length > 0 %}
    There are {{ comments | length }} comments
{% else %}
    There are no comments
{% endif %}
```


# 2. 循环
我们可以在 Jinja2 中使用循环来迭代任何迭代器
```htm
{% for post in posts %}
<div>
<h1>{{ post.title }}</h1>
<p>{{ post.text | safe }}</p>
</div>
{% endfor %}
```

for循环和if语句可以组合使用，以模拟 Python 循环中的 continue 功能，下面这个循环将只会渲染post.text不为None的那些post：
```htm
{% for post in posts if post.text %}
<div>
<h1>{{ post.title }}</h1>
<p>{{ post.text | safe }}</p>
</div>
{% endfor %}
```

在循环内部,你可以使用一个叫做loop的特殊变量来获得关于for循环的一些信息

比如：要是我们想知道当前被迭代的元素序号，并模拟Python中的enumerate函数做的事情，则可以使用loop变量的index属性,例如:

```htm
{% for post in posts%}
{{loop.index}}, {{post.title}}
{% endfor %}
```

数据结果如下：
1, Post title
2, Second Post

在一个 for 循环块中你可以访问这些特殊的变量:
变量	描述
loop.index	当前循环迭代的次数（从 1 开始）
loop.index0	当前循环迭代的次数（从 0 开始）
loop.revindex	倒序，当前循环迭代的次数（从 1 开始）
loop.revindex0	倒序，当前循环迭代的次数（从 0 开始）
loop.first	如果是第一次迭代，为 True
loop.last	如果是最后一次迭代，为 True
loop.length	序列中的项目数

# 3. 示例程序
实现的效果


准备数据
# 只显示4行数据，背景颜色依次为：黄，绿，红，紫
```python
my_list = [
    {
        "id": 1,
        "value": "我爱工作"
    },
    {
        "id": 2,
        "value": "工作使人快乐"
    },
    {
        "id": 3,
        "value": "沉迷于工作无法自拔"
    },
    {
        "id": 4,
        "value": "日渐消瘦"
    },
    {
        "id": 5,
        "value": "以梦为马，越骑越傻"
    }
]
```

模板代码
```htm
{% for item in my_list if item.id != 5 %}
    {% if loop.index == 1 %}
        <li style="background-color: orange">{{ item.value }}</li>
    {% elif loop.index == 2 %}
        <li style="background-color: green">{{ item.value }}</li>
    {% elif loop.index == 3 %}
        <li style="background-color: red">{{ item.value }}</li>
    {% else %}
        <li style="background-color: purple">{{ item.value }}</li>
    {% endif %}
{% endfor %}
```

