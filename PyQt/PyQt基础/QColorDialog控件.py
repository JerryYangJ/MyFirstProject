# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QColorDialog控件.py
# @Info  : 颜色对话框


'''



'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class ColorDialog(QtWidgets.QWidget):
    def __init__(self):
        super(ColorDialog, self).__init__()

        self.setWindowTitle("颜色对话框演示程序")
        self.setGeometry(300, 300, 250, 180)

        self.button = QtWidgets.QPushButton("更改颜色", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        self.button.clicked.connect(self.show_dialog)
        self.setFocus()     # 将当前窗口设为焦点窗口，即设为选中状态

        color = QtGui.QColor(0, 0, 0)   #调用QtGui.QColor用rgb值给颜色赋值，然后再调用它的.name方法便能方便的得到各种颜色的名字便于我们进行颜色的设置。
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("QWidget{background-color:%s}"% color.name())     # setStyleSheet方法用来设置图形界面的外观,setStyleSheet的语法，它接受一个字符串，字符串的开始是调用这个方法的实例的类，应该只能是PyQt中的类（个人理解），然后花括号扩起来的是设置，这里background-color是指背景颜色，然后用了一个占位符，对应的是后面的color.name()
        self.widget.setGeometry(130, 22, 100, 100)

    def show_dialog(self):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            self.widget.setStyleSheet("QWidget{background-color:%s}" % col.name())


app = QtWidgets.QApplication(sys.argv)
colordialog = ColorDialog()
colordialog.show()
sys.exit(app.exec_())



