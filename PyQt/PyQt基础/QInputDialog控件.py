# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QInputDialog控件.py
# @Info  : 输入对话框

'''
QInputDialog常用方法：
    getint()：从输入控件中获得标准整数输入
    getDouble()：从输入控件中获得标准浮点数输入
    getText()：从输入控件中获得标准字符串的输入
    getItem() ：从输入控件中获得列表里的选项输入

关键代码介绍：
    QInputDialog.getInt(self, 'Integer input dialog', '输入数字') -> 输入整数对话框
    QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：') -> 输入字符串对话框
    QInputDialog.getItem(self, "select input dialog", '语言列表', items, 0, False) -> 下拉列表选择对话框
'''


# -*- coding: utf-8 -*-
"""输入对话框示例"""
import sys
from PyQt5 import QtWidgets, QtCore

class InputDialog(QtWidgets.QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle("输入对话框演示程序")
        self.setGeometry(300, 300, 350, 80)
        self.button = QtWidgets.QPushButton("对话框", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)
        self.setFocus()         # 将当前窗口设为焦点窗口，即设为选中状态
        self.label = QtWidgets.QLineEdit(self)
        self.label.move(130, 22)

    def show_dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "输入对话框", "请输入你的名字：")
        if ok:
            self.label.setText(text)

app = QtWidgets.QApplication(sys.argv)
input_dialog = InputDialog()
input_dialog.show()
sys.exit(app.exec_())



