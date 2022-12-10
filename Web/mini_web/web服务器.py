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

g_documengts_root = './html'


def main():
    # 1.创建套接字
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定本地信息
    sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 防止端口未完全释放，无法使用的问题
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
        ret = re.match(r'([^/]*)(/[^ ]*)', request_lines[0])
        if ret:
            print("正则提出数据：", ret.group(1), ret.group(2))
            file_name = ret.group(2)
            if file_name == '/':
                file_name = '/index.html'
            print("文件名：", file_name)
        # 读取文件数据
        try:
            f = open(g_documengts_root + file_name, 'rb')
            print("读取的文件：", g_documengts_root + file_name)
        except:
            response_header = "HTTP/1.1 404 file not found \r\n"    # <版本号>+<状态码>+<状态码解释>
            response_header += "Content-Type: text/html; charset=utf-8 \r\n"    # key: value \r\n
            response_header += "\r\n"   # 分离报头和有效载荷（body）
            response_body = "file not found,请输入正确的地址"

            # response = response_header + response_body
            # 将header返回给浏览器
            new_socket.send(response_header.encode('utf-8'))
            # 将body返回给浏览器
            new_socket.send(response_body.encode('utf-8'))
        else:
            content = f.read()

            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "\r\n"
            response_body = content

            # response = response_header + response_body
            # 将header返回给浏览器
            new_socket.send(response_header.encode('utf-8'))
            # 将body返回给浏览器
            new_socket.send(response_body)
            # 关闭文件
            f.close()
        finally:
            # 关闭这个新套接字
            new_socket.close()


if __name__ == "__main__":
    main()
