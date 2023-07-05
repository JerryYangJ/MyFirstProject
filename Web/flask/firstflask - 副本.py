# @Time :2022/9/15 9:29
# @Author : Jerry Y
# @File  : firstflask.py
# @Info  :
from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return "哈哈哈，我是第一个flask页面，成功的道路开始了。。。。"


@app.route("/profile")
def profile():
    return "<h1>我是个人主页<h1>"


@app.route("/profile1")
def profile1():
    # 打开profile.html文件，读取文件
    with open("profile.html") as f:
        content = f.read()
    return content


# 路由传参
@app.route("/profile2/<user_name>")
def profile2(user_name):
    return f"<h1>我是{user_name}的个人主页<h1>"


@app.route("/profile3/<user_name>")
def profile3(user_name):
    # 打开profile.html文件，读取文件
    with open("profile.html") as f:
        content = f.read()
        content = content.replace('James Doe', user_name)
    return content


# 重定向redirect(需要导入），使用url_for,直接写对应的视图函数名
@app.route("/profile4")
def profile4():
    # return redirect(url_for('profile'))
    return redirect("http://www.baidu.com")


# 带参数
@app.route("/profile5/<user_name>")
def profile5(user_name):
    return render_template("profile2.html", user_name=user_name)


# 多参数
@app.route("/profile6/<user_name>/<user_image>")
def profile6(user_name, user_image):
    return render_template("profile6.html", user_name=user_name, user_image=user_image)


# 多参数
@app.route("/profile7/<user_name>")
def profile7(user_name):
    return render_template("profile7.html", user_name=user_name)

app.run(debug=True)
# app.run()
print(app.url_map)  # url_map 将装饰器路由和视图的对应关系保存起来
