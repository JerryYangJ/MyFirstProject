# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QCalendarWidget控件.py
# @Info  : 日历


'''
QCalendarWidget 类提供了以月为单位的日历部件。该部件允许用户以一种简单而直接的方式选择日期。

信号
    selectionChanged()
'''

import sys
from PyQt5 import QtWidgets, QtCore


class CalendarWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CalendarWidget, self).__init__()

        self.setWindowTitle("日历部件演示程序")
        self.setGeometry(300, 300, 350, 300)

        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.show_date)

        date = self.calendar.selectedDate()
        self.label = QtWidgets.QLabel(self)
        self.label.setText(str(date.toPyDate()))

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.calendar)
        v_box.addWidget(self.label)
        self.setLayout(v_box)

    def show_date(self):
        date = self.calendar.selectedDate()
        self.label.setText(str(date.toPyDate()))


app = QtWidgets.QApplication(sys.argv)
cw = CalendarWidget()
cw.show()
sys.exit(app.exec_())






