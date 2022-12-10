# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : PyQt实战1：图片浏览器.py
# @Info  : 实现一个图片浏览器，使用左右按钮控制图片加载。思路：从电脑文件夹选择文件名称，通过左右按钮改变字典索引显示文件
# 待增加功能：图片缩放适应大小


import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QWidget, QScrollArea


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.label_dis = None
        self.pageNum = 0
        self.file_lst = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1229, 820)
        # 图片显示标签
        self.label_dis = QtWidgets.QLabel(Form)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setWidget(self.label_dis)
        self.label_dis.setGeometry(QtCore.QRect(10, 10, 3840, 2160))
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 1211, 751))
        self.label_dis.setObjectName("label_dis")
        # self.label_dis.setScaledContents(False)

        # 设置居中对齐
        self.label_dis.setAlignment(Qt.AlignCenter)
        # 设置提示信息
        self.label_dis.setToolTip('图片标签')
        self.label_dis.setPixmap(QPixmap("D:\图片\地图.png").scaledToWidth(751))

        self.pushButton_up = QtWidgets.QPushButton(Form)
        self.pushButton_up.setGeometry(QtCore.QRect(490, 780, 75, 23))
        self.pushButton_up.setObjectName("pushButton_up")
        self.pushButton_down = QtWidgets.QPushButton(Form)
        self.pushButton_down.setGeometry(QtCore.QRect(590, 780, 75, 23))
        self.pushButton_down.setObjectName("pushButton_down")

        self.pushButton_filePath = QtWidgets.QPushButton(Form)
        self.pushButton_filePath.setGeometry(QtCore.QRect(10, 780, 75, 23))
        self.pushButton_filePath.setObjectName("pushButton_filePath")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 780, 371, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_filePath.clicked.connect(self.label_setText)
        self.pushButton_down.clicked.connect(self.photoDown)
        self.pushButton_up.clicked.connect(self.photoUp)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片浏览器"))
        self.pushButton_up.setText(_translate("Form", "上一张"))
        self.pushButton_down.setText(_translate("Form", "下一张"))
        self.pushButton_filePath.setText(_translate("Form", "打开文件夹"))
        self.label.setText(_translate("Form", "TextLabel"))

    def label_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        self.file_lst, type = QFileDialog.getOpenFileNames(None, "请选择文件", "D:/图片", "Text File(*.png *.jpg);; Image(*.jpeg)")  # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.label.setText(self.file_lst[0])
        self.label_dis.setPixmap(QPixmap(self.file_lst[0]).scaled(1211, 751))

    def photoDown(self):
        if self.pageNum <= len(self.file_lst) - 2:
            self.pageNum += 1
            print(self.pageNum)
            self.label_dis.setPixmap(QPixmap(self.file_lst[self.pageNum]))
        else:
            QMessageBox.warning(self, "Warning", "这是最后一张图片")

    def photoUp(self):
        if self.pageNum >= 1:
            self.pageNum -= 1
            print(self.pageNum)
            self.label_dis.setPixmap(QPixmap(self.file_lst[self.pageNum]))
        else:
            QMessageBox.warning(self, "Warning", "这是第一张图片")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
