# @Time :2022/11/7 9:44
# @Author : Jerry Y
# @File  : QCombBox控件.py
# @Info  : 下拉列表

'''
方法：
    currentText()   获取选择的值

'''
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QComboBox


class MyQComboBox(QtWidgets.QWidget):

    def __init__(self):
        super(MyQComboBox, self).__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        self.lbl1 = QLabel("1", self)

        self.combo = QComboBox(self)
        self.combo.addItem("Ubuntu")
        self.combo.addItem("Windows")
        self.combo.addItem("centos")
        self.combo.addItem("deepin")
        self.combo.addItem("redhat")
        self.combo.addItem("debain")
        self.combo.move(50, 50)
        self.lbl.move(50, 150)
        self.combo.activated[str].connect(self.onActivated)

        self.combo1 = QComboBox(self)
        self.combo1.addItem("1")
        self.combo1.addItem("2")
        self.combo1.addItem("3")
        self.combo1.move(200, 50)
        self.lbl1.move(200, 150)
        self.combo1.currentIndexChanged.connect(self.combo1_onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('下拉选框练习 ')
        self.show()


    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

    def combo1_onActivated(self):
        self.lbl1.setText(self.combo1.currentText())


app = QApplication(sys.argv)
ex = MyQComboBox()
sys.exit(app.exec_())
