# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QProgressBar控件.py
# @Info  : 进度条


'''
进度条部件。因为使用进度条可以形象告诉用户当前的任务正在进行中。PyQt5 工具包提供了水平和垂直两种类型的进度条部件。我们可以设置进度条的最大和最小值，默认的最大和最小值分别为 0 和 99。
'''

# -*- coding: utf-8 -*-
"""进度条示例"""
import sys
from PyQt5 import QtWidgets, QtCore


class ProgressBar(QtWidgets.QWidget):
    def __init__(self):
        super(ProgressBar, self).__init__()

        self.setWindowTitle("进度条演示程序")
        self.setGeometry(300, 300, 250, 150)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)

        self.button = QtWidgets.QPushButton("开始", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)
        self.button.clicked.connect(self.on_start)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def timerEvent(self, *args, **kwargs):
        """每一个 QObject 对象或其子对象都有一个QObject.timerEvent 方法。在本实例中，为了响应定时器的超时事件，我们需要使用上面的代码重写进度条的 timerEvent 方法。"""
        if self.step >= 100:
            self.timer.stop()
            return
        self.step += 1
        self.progress_bar.setValue(self.step)

    def on_start(self):
        """要激活该进度条，我们需要使用定时器的start()方法启动定时器。该方法的第一个参数为超时时间。第二个参数表示当前超时时间到了以后定时器触发超时事件的接收对象。"""
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText("开始")
        else:
            self.timer.start(100, self)
            self.button.setText("停止")

app = QtWidgets.QApplication(sys.argv)
pb = ProgressBar()
pb.show()
sys.exit(app.exec_())





