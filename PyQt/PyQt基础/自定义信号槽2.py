"""
@author: JerryYang
@file: 自定义信号槽2.py
@time: 2023/5/4 14:18
@desc:
"""
import sys
import time

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


# 通过类变量定义信号对象，在__init__函数前定义自定义信号
class MainWindow(QWidget):
    # 定义无参数的信号
    noParameterSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义槽函数")
        self.resize(800, 600)

        button = QPushButton("close", self)

        # 连接内置信号与内置槽函数close
        button.clicked.connect(self.onclick)

        # 将自定义信号分别连接两个槽函数，连接顺序不同，执行顺序就不同
        self.noParameterSignal.connect(self.oneSlot)
        self.noParameterSignal.connect(self.twoSlot)

    def onclick(self):
        """ 点击按钮后发送自定义信号 """
        self.noParameterSignal.emit()

    def oneSlot(self):
        """ 第一个槽函数 """
        print("第一个槽函数执行")
        time.sleep(2)

    def twoSlot(self):
        """ 第二个槽函数"""
        print("第二个槽函数执行")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
