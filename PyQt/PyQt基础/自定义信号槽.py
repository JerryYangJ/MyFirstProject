"""
@author: JerryYang
@file: 自定义信号槽.py
@time: 2023/5/4 8:16
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
    # 定义一个参数的信号， 参数类型为int
    oneParameterSignal = pyqtSignal(int)
    # 定义一个参数的重载版本的信号， 参数类型为int或str
    oneParameterOverloadSignal = pyqtSignal([int], [str])
    # 定义两个参数的重载版本的信号， 参数类型为int,str或int,int
    twoParameterOverloadSignal = pyqtSignal([int, str], [int, int])
    # 定义一个list类型参数的信号
    oneParameterSignalList = pyqtSignal(list)
    # 定义一个dict类型参数的信号
    oneParameterSignalDict = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("自定义槽函数")
        self.resize(800, 600)

        button = QPushButton("close", self)

        # 连接内置信号与内置槽函数close
        button.clicked.connect(self.onNoParameterSlot)
        # 连接自定义信号与自定义槽
        self.oneParameterSignal.connect(lambda: self.onOneParameterSlot(1))
        self.twoParameterOverloadSignal.connect(lambda: self.onTwoParameterSlot(1, "接收信号"))

    def onNoParameterSlot(self):
        """
        定义无参数的槽函数
        注意顺序，信号执行优先级高
        """
        print("发送无参数信号")
        self.oneParameterSignal.emit(1)

    def onOneParameterSlot(self, nIndex):
        """ 定义一个参数的槽函数，参数为整形"""
        print("发送一个参数信号")
        self.twoParameterOverloadSignal.emit(1, "接收信号")

    def onTwoParameterSlot(self, nIndex, sStatus):
        """ 定义两个参数的槽函数，参数为整形，字符串型"""
        print(nIndex, sStatus)
        # self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
