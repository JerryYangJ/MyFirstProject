# @Time :2022/9/15 9:29
# @Author : Jerry Y
# @File  : firstflask.py
# @Info  :
from flask import Flask, redirect, url_for, jsonify
from flask import render_template

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def index():
    return "哈哈哈，我是第一个flask页面，成功的道路开始了。。。。"


@app.route("/profile")
def profile():
    return "<h1>我是个人主页<h1>"


@app.route("/profile1")
def profile1():
    # 打开profile.html文件，读取文件
    with open("Web/flask/profile.html") as f:
        content = f.read()
    return content


# 路由传参
@app.route("/profile2/<user_name>")
def profile2(user_name):
    return f"<h1>我是{user_name}的个人主页<h1>"


# 返回json数据：使用jsonify 生成一个 JSON 的响应.不推荐使用 json.dumps 转成 JSON 字符串直接返回，因为返回的数据要符合 HTTP 协议规范，如果是 JSON 需要指定 content-type:application/json
@app.route("/json")
def json():
    json_dic = {
        'userID': 10,
        'userName': "JerryYang"
    }
    return jsonify(json_dic)


@app.route("/profile3/<user_name>")
def profile3(user_name):
    # 打开profile.html文件，读取文件
    with open("Web/flask/profile.html") as f:
        content = f.read()
        content = content.replace('James Doe', user_name)
    return content

# 自定义状态码
@app.route('/demo6')
def demo6():
    return '状态码为 666', 666


# 重定向redirect(需要导入）
@app.route("/profile4")
def profile4():
    # return redirect(url_for('profile'))   # 使用url_for,直接写对应的视图函数名
    return redirect("http://www.baidu.com")     # 可以直接填写自己 url 路径


# 使用模板
@app.route("/profile5/<user_name>")
def profile5(user_name):
    return render_template("profile2.html", user_name=user_name)


# 使用模板
@app.route("/profile6/<user_name>/<user_image>")
def profile6(user_name, user_image):
    return render_template("profile6.html", user_name=user_name, user_image=user_image)


# 使用模板
@app.route("/profile7/<user_name>")
def profile7(user_name):
    return render_template("profile7.html", user_name=user_name)

# 读取文件内容替换模板显示内容
@app.route("/profile8/<user_name>/<profile_info>")
def profile8(user_name, profile_info):
    try:
        with open(f"Web/flask/templates/{user_name}.txt", 'r', encoding='utf-8')as f:
            lines_list = f.readlines()
            user_name = lines_list[0]
            profile_info = ''.join(lines_list[1:])
        return render_template("profile8.html", user_name=user_name, profile_info=profile_info)
    except:
        return f"对不起，没有找到'{user_name}'的信息"

        


app.run(debug=True)
# app.run()
print(app.url_map)  # url_map 将装饰器路由和视图的对应关系保存起来
