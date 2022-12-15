from flask import Blueprint

# 创建一个蓝图，用来管理多个函数视图
index_blu = Blueprint("index", __name__)

from . import views