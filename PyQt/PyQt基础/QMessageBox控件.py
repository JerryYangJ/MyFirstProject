# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QMessageBox控件.py
# @Info  : 消息对话框


'''
QMessageBox类中常用方法
    information(QWidget parent,title,text,buttons,defaultButton)：弹出消息对话框。
    question(QWidget parent,title,text,buttons,defaultButton)：弹出问答对话框
    warning(QWidget parent,title,text,buttons,defaultButton)：弹出警告对话框
    critical(QWidget parent,title,text,buttons,defaultButton)：弹出严重错误对话框
    about(QWidget parent,title,text)：弹出关于对话
      参数解释如下：
        parent：指定的父窗口控件。
        title：表示对话框标题。
        text：表示对话框文本。
        buttons：表示多个标准按钮，默认为ok按钮。
        defaultButton表示默认选中的标准按钮，默认选中第一个标准按钮。

其他方法如下：
    setTitle()：设置标题
    setText()：设置正文消息
    setIcon()：设置弹出对话框的图片

QMessageBox的标准按钮类型
    QMessage.Ok 同意操作、
    QMessage.Cancel  取消操作
    QMessage.Yes  同意操作
    QMessage.No  取消操作
    QMessage.Abort  终止操作
    QMessage.Retry 重试操作
    QMessage.Ignore  忽略操作


'''

import sys

from PyQt5.QtWidgets import QLabel, QApplication, QPushButton, QWidget,  QMessageBox


class MyMessageBox(QWidget):
    def __init__(self):
        super(MyMessageBox, self).__init__()

        self.setWindowTitle("对话框控件演示")
        self.setGeometry(100, 50, 800, 800)

        self.button_info = QPushButton("消息对话框", self)
        self.button_info.move(20, 20)

        self.button_q = QPushButton("问答对话框", self)
        self.button_q.move(20, 60)

        self.button_w = QPushButton("警告对话框", self)
        self.button_w.move(20, 100)

        self.button_c = QPushButton("严重错误对话框", self)
        self.button_c.move(20, 140)

        self.button_a = QPushButton("关于对话框", self)
        self.button_a.move(20, 180)

        self.label = QLabel("显示点击选择结果", self)
        self.label.move(20, 240)

        self.button_info.clicked.connect(self.btn_info_slot)
        self.button_q.clicked.connect(self.bti_q_slot)
        self.button_w.clicked.connect(self.bti_w_slot)
        self.button_c.clicked.connect(self.bti_c_slot)
        self.button_a.clicked.connect(self.bti_a_slot)

    def btn_info_slot(self):
        result = QMessageBox.information(self, "这是消息对话框标题", "这是消息对话框的信息内容")
        if result:
            self.label.setText("点击了确定")

    def bti_q_slot(self):
        result = QMessageBox.question(self, "这是问答对话框", "你确定要退出么？")  # 返回值是  QMessage.Yes  同意操作/QMessage.No  取消操作
        if result == QMessageBox.Yes:
            self.label.setText("你选择了退出")
        else:
            self.label.setText("你选择了不退出")

    def bti_w_slot(self):
        result = QMessageBox.warning(self, "这是警告对话框", "警告一下？")

    def bti_c_slot(self):
        result = QMessageBox.question(self, "严重错误对话框", "出现一个严重错误")  # 返回值是
        if result == QMessageBox.Yes:
            self.label.setText("你选择了Yes")
        else:
            self.label.setText("你选择了No")

    def bti_a_slot(self):
        result = QMessageBox.question(self, "关于对话框", "关于。。。。你知道吗")  # 返回值是
        if result == QMessageBox.Yes:
            self.label.setText("你选择了Yes")
        else:
            self.label.setText("你选择了No")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyMessageBox()
    win.show()

    app.exec_()
