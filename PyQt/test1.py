# @Time :2022/10/26 14:34
# @Author : Jerry Y
# @File  : test1.py
# @Info  :
import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('test1.ui')
        # print(self.ui.__dict__)

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit
        self.password_qwidget = self.ui.lineEdit_2
        self.login_btn = self.ui.pushButton
        self.forget_password_btn = self.ui.pushButton_2
        self.textBrowser = self.ui.textBrowser

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login)

    def login(self):
        """登录按钮的槽函数"""
        user_name = self.user_name_qwidget.text()
        possword = self.password_qwidget.text()

        if user_name == 'admin' and possword == '123':
            self.textBrowser.setText(f"欢迎{user_name}")
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText("用户名或密码错误。。。。请重试")
            self.textBrowser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建窗口对象
    w = MyWindow()
    # 显示窗口
    w.ui.show()

    app.exec()
