# @Time :2022/11/3 11:54
# @Author : Jerry Y
# @File  : QScrollArea控件.py
# @Info  : 滚动区

'''
QScrollArea滚动区组件用来显示子控件的内容的框架，如果子控件的尺寸超过了框架的大小，可以使用滚动条，方便查看整个子控件。QScrollArea可以给任何
QWidget添加滚动条，但一般自定义窗体添加滚动条不显示
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QPushButton, QTableView


class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        # 滚动区创建
        self.scrollArea = QScrollArea()
        # 容器组件
        widget  = QWidget()
        layout = QVBoxLayout()
        tableView = QTableView()
        button = QPushButton("OK")
        layout.addWidget(tableView)
        layout.addWidget(button)
        widget.setLayout(layout)
        # 设置滚动区的容器组件
        self.scrollArea.setWidget(widget)
        self.layout.addWidget(self.scrollArea)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
