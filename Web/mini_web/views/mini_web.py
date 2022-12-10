# @Time :2022/9/12 19:22
# @Author : Jerry Y
# @File  : mini_web.py
# @Info  :
import time
from contextlib import contextmanager

# 定义一个字典，用于存储url以及对应的func的对应关系：
URL_ROUTE = {}
# 定义一个变量，存储html文件路径
TEMPLATE_PATH = "./templates"


@contextmanager
def mini_open(file_path, mode='r'):
    file_path = file_path.replace('.py', '.html')
    f = open(TEMPLATE_PATH + file_path, mode, encoding='utf-8')
    yield f
    f.close()


def route(url):
    def set_func(func):
        URL_ROUTE[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


# @route('./index.py')
# def index(url_file):
#     with mini_open(url_file) as f:
#         html_content = f.read()
#     return html_content
@route("/index.py")
def index(url_file):  # -------- 更新 ---------
    # -------- 更新 ---------
    with mini_open(url_file) as f:
        html_content = f.read()
    return html_content


@route('/login.py')
def login(url_file):
    return f"当前是登录页面login，当前时间是：{time.ctime()}"


@route('/logout.py')
def logout(url_file):
    return f"当前是退出页面logout，当前时间是：{time.ctime()}"


@route('/register.py')
def register(url_file):
    return f"当前是注册页面register，当前时间是：{time.ctime()}"


# @route('/page_404.py')
def page_404(url_file):
    return f"404，当前时间是：{time.ctime()}"


#
# URL_ROUTE = {
#     '/login.py': login,
#     '/logout.py': logout,
#     '/register.py': register,
#     '404': page_404
# }


def application(env, call_func):
    """ 根据文件路径，在URL_ROUTE字典中找出映射对应的函数"""
    # 文件路径
    file_path = env['PATH_INFO']
    func = URL_ROUTE.get(file_path, None)
    if not func:
        # 回调call_func变量指向的函数，并且将状态码及header传过去
        call_func("404 Not Found", [("Content-Type", "text/html; charset=utf-8")])
        response_body = page_404(file_path)
    else:
        # 回调call_func变量指向的函数，并且将状态码及header传过去
        call_func("200 ok", [("Content-Type", "text/html; charset=utf-8"), ("framework", "mini_web")])
        # 函数的引用：
        # 调用函数
        response_body = func(file_path)

    # 返回response_body给浏览器
    return response_body


"""--------------------另一种写法------------------"""
# def application(env, call_func):
#     """ 根据文件路径，在URL_ROUTE字典中找出映射对应的函数"""
#     # 文件路径
#     file_path = env['PATH_INFO']
#     # func = URL_ROUTE.get(file_path, None)
#     if file_path not in URL_ROUTE.keys():
#         # 回调call_func变量指向的函数，并且将状态码及header传过去
#         call_func("404 Not Found", [("Content-Type", "text/html; charset=utf-8")])
#         response_body = page_404()
#     else:
#         # 回调call_func变量指向的函数，并且将状态码及header传过去
#         call_func("200 o---k", [("Content-Type", "text/html; charset=utf-8"), ("framework", "mini_web")])
#         # 函数的引用：
#         func = URL_ROUTE[file_path]
#         # 调用函数
#         response_body = func()
#
#     # 返回response_body给浏览器
#     return response_body

"""-----------------以下为测试代码----------------"""


# def set_status_headers(status, headers):
#     status = status  # "200 ok"
#     headers = headers  # [("Content-Type", "text/html; charset=utf-8 ")])
#     # print(status, '\n', headers)
#
# print(URL_ROUTE)
#
# env = {'PATH_INFO': '/login.py'}
#
# response_body = application(env, set_status_headers)
# print(response_body)
