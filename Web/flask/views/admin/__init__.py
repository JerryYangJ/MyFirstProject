from flask import Blueprint

# 创建一个蓝图，用来管理多个函数视图
admin_blu = Blueprint("admin", __name__)

from . import views