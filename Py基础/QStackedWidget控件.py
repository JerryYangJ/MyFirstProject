# @Time :2022/11/3 11:47
# @Author : Jerry Y
# @File  : QStackedWidget控件.py
# @Info  : 栈式容器

'''
QStackedWidget是栈式容器组件，开发人员可以使用栈管理控件，QStackedWidget只显示栈顶的控件，使用raiseWidget函数把栈中任何其他控件移到栈顶，
从而实现控件之间的切换。

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QPushButton


class MainWidget(QWidget):
    currentIndex = 0
    N = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stackWidget = QStackedWidget(self)
        self.layout = QVBoxLayout()

        button = QPushButton("Next")
        button.clicked.connect(self.onNext)
        self.layout.addWidget(self.stackWidget)
        self.layout.addWidget(button)
        self.setLayout(self.layout)

    def initUI(self):
        for i in range(self.N):
            button = QPushButton()
            button.setText("Button {0}".format(i))
            self.stackWidget.addWidget(button)

    def onNext(self):
        self.currentIndex = self.currentIndex + 1
        print(self.currentIndex)
        self.currentIndex = self.currentIndex % self.N      # 妙：一个巧妙的控制方法，值得学习
        # print(self.currentIndex)
        self.stackWidget.setCurrentIndex(self.currentIndex)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
