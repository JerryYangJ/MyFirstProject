from flask import Flask, redirect, url_for, jsonify,request
from flask import render_template
from . import admin_blu



# 使用模板，读取文件数据，更新到模板
@admin_blu.route("/index.html")
def admin_index():
    return render_template("admin/index.html")

# 登录页面
@admin_blu.route("/login")
def admin_login():
    ret = request.args
    if ret:
        user_name = ret.get('Username')
        passwd = ret.get('Password')
        if user_name == "jerry" and passwd == '123456':
            return f"登录成功。。。。用户名：{user_name},密码：{passwd}"
        else:
            return render_template("admin/login.html")
    else:
        return render_template("admin/login.html")


@admin_blu.route("/basic-table.html")
def basic_table():
    # with open("Web/flask/templates/admin/basic-table copy.html",'r', encoding='utf-8')as f:
    #     content = f.read()
    #     return content
    user_infos = [["1", "张三", "28", "10000"],
                  ["2", "李四", "24", "12000"],
                  ["3", "王五", "22", "15000"]
                  ]
    return render_template("admin/basic-table copy.html", user_infos=user_infos)
