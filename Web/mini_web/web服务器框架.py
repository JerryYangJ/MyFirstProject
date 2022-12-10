# @Time :2022/9/10 17:24
# @Author : Jerry Y
# @File  : web服务器.py
# @Info  :
"""
/r/n是什么意思？
大家都知道，通过网络传输，传输的都是bit位（由Byte字节转换），服务端接受到http request部分后，读出来的数据也是Byte流。服务端是怎样截取Byte流的，比如什么时候header结束，http body开始。
通过两个连续的字节13和10（也就是\r\n）。表示http header结束，http body开始
"""
import re
import socket
import sys
import threading

# 定义一个全局变量，用来存储加载框架mini_web的路径
VIEW_PATH = "./views"


class WSGIServer(object):
    """定义一个WSGI服务器类"""

    def __init__(self, port, app):
        self.new_socket = None
        self.documents_root = './static'
        # 1.创建套接字
        self.sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.绑定本地信息
        self.sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 防止端口未完全释放，无法使用的问题
        self.sever_socket.bind(("", port))
        # 3.变为监听套接字
        self.sever_socket.listen(128)
        # 4.定义两个属性，存储web框架传递过来的状态码及响应头
        self.status = ""  # 指向状态码字符串
        self.headers = None  # 指向一个新的列表
        # 定义属性，存储web框架入口函数的引用
        self.app = app

    def run_forever(self):
        """运行服务器"""
        # 4.等待对方链接
        while True:
            self.new_socket, new_addr = self.sever_socket.accept()
            new_thread = threading.Thread(target=self.deal_with_request)  # 创建进程
            new_thread.start()  # 线程的套接字不需要关闭（进程复制，线程共享）

    def deal_with_request(self):
        """为这个浏览器服务"""
        # 接收数据
        request = self.new_socket.recv(1024).decode('utf-8')
        # print(request)
        if not request:
            return

        request_lines = request.splitlines()
        # for i, line in enumerate(request_lines):
        #     print(i, line)
        # 提取请求的文件（index.html)
        ret = re.match(r'([^/]*)(/[^ ]*)', request_lines[0])
        if ret:
            # print("正则提出数据：", ret.group(1), ret.group(2))
            file_name = ret.group(2)
            if file_name == '/':
                file_name = '/index.html'
            # print("文件名：", file_name)
        if not file_name.endswith(".py"):
            # 读取文件数据
            try:
                # 从html文件夹中读取对应的文件数据内容
                with open(self.documents_root + file_name, 'rb') as f:
                    content = f.read()
                print("读取的文件路径：",  self.documents_root + file_name)
            except Exception:
                # 如果有异常，那么认为：找不到对应的文件，此时就应该对浏览器返回404
                response_header = "HTTP/1.1 404 file not found\r\n"  # <版本号>+<状态码>+<状态码解释>
                response_header += "Content-Type: text/html; charset=utf-8\r\n"  # key: value \r\n
                response_header += "\r\n"  # 分离报头和有效载荷（body）
                response_body = "file not found,请输入正确的地址"

                response = response_header + response_body
                # 将response返回给浏览器
                self.new_socket.send(response.encode('utf-8'))
            else:
                response_header = "HTTP/1.1 200 OK\r\n"
                response_header += "\r\n"
                response_body = content

                response = response_header.encode('utf-8') + response_body
                # 将response返回给浏览器
                self.new_socket.send(response)
        else:
            """如果是以.py结尾的请求，则进行动态生成页面内容"""
            # 定义一个字典，用来封装数据，传入application函数中
            env = dict()  # env ={}
            # 将文件路径封装到env字典中
            env['PATH_INFO'] = file_name
            response_body = self.app(env, self.set_status_headers)

            response_header = f"HTTP/1.1 {self.status}\r\n"  # <版本号>+<状态码>+<状态码解释>
            # response_header = f"HTTP/1.1 404 OK\r\n"  # <版本号>+<状态码>+<状态码解释>
            # print(response_header)
            for header in self.headers:
                response_header += f"{header[0]}:{header[1]}\r\n"  # key: value \r\n
            response_header += "\r\n"  # 分离报头和有效载荷（body）
            # print(response_header)

            # response = response_header + response_body
            self.new_socket.send(response_header.encode('utf-8'))
            self.new_socket.send(response_body.encode('utf-8'))
        # # 关闭这个新套接字(使用进程时需要关闭，使用线程不需要关闭
        # self.new_socket.close()

    def set_status_headers(self, status, headers):
        self.status = status  # "200 ok"
        self.headers = headers  # [("Content-Type", "text/html; charset=utf-8")])
        # print(status)


def main():
    # 运行参数 python3 xxx.py port frame_module:app_name
    # 获取运行参数：sys.argv
    if len(sys.argv) == 3:
        # 获取web服务器的port(运行参数的第二个参数）
        port = sys.argv[1]
        if port.isdigit():  # 如果port是数字类型的字符串，转为数字
            port = int(port)
        else:
            exit("请输入数字类型的端口号")
        # 获取web服务器对应的web框架名字
        web_frame_module_app_name = sys.argv[2]
    else:
        exit("请按此格式运行：python3 <xxx>.py <port> <frame_module:app_name>")
    print("服务器使用的端口为：", port)
    # 从web_frame_module_app_name中提取框架名web_frame_module及入口函数app_name
    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    # print(web_frame_module_app_name)
    ret = re.match(r"(.*?):(.*)", web_frame_module_app_name)
    web_frame_module_name = ret.group(1)
    app_name = ret.group(2)
    print("使用的服务器框架：", web_frame_module_name, '\n', "框架入口函数：", app_name)

    # 添加导入框架时查找的路径，保证框架能找到
    sys.path.insert(0, VIEW_PATH)
    # 导入框架
    web_frame_module = __import__(web_frame_module_name)
    # 获取框架内可以直接调用的函数（对象）
    app = getattr(web_frame_module, app_name)

    # 创建服务器对象
    http_server = WSGIServer(port, app)
    http_server.run_forever()


if __name__ == "__main__":
    main()
