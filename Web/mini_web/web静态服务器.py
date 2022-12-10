# @Time :2022/9/10 17:24
# @Author : Jerry Y
# @File  : web服务器.py
# @Info  :

#http://127.0.0.1:8888/

import socket

g_documengts_root = './html'
def main():
    # 1.创建套接字
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定本地信息
    sever_socket.bind(("", 8888))
    # 3.变为监听套接字
    sever_socket.listen(128)
    # 4.等待对方链接
    while True:
        new_socket, new_addr = sever_socket.accept()
        # 接收数据
        request = new_socket.recv(1024).decode('utf-8')
        print(request)
        request_lines = request.splitlines()
        for i, line in enumerate(request_lines):
            print(i, line)
        # 提取请求的文件（index.html)
        ret = re.match(r"([^/]*)(/[^ ]+)", request_lines[0])
        if ret:
            print("正则提出数据：", ret.group(1), ret.group(2))
            file_name = ret.group(2)
        # 读取文件数据
        f = open(g_documengts_root + file_name, 'rb')
        content = f.read()

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header +="\r\n"
        response_body = "content"

        # response = response_header + response_body
        # 将header返回给浏览器
        new_socket.send(response_header.encode('utf-8'))
        # 将body返回给浏览器
        new_socket.send(response_body)
        # 关闭这个新套接字
        new_socket.close()

if __name__ == "__main__":
    main()
