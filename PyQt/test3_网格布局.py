# @Time :2022/11/3 13:55
# @Author : Jerry Y
# @File  : test3_网格布局.py
# @Info  :
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QSizePolicy


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QGridLayout()
        self.layout.setSpacing(5)
        button = QPushButton("Button1")
        button.setMinimumSize(60, 30)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout.addWidget(button, 0, 0, 1, 1)

        button = QPushButton("Button2")
        button.setMinimumSize(60, 30)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout.addWidget(button, 0, 1, 1, 1)

        button = QPushButton("Button3")
        button.setMinimumSize(60, 30)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout.addWidget(button, 1, 0, 1, 1)

        button = QPushButton("Button4")
        button.setMinimumSize(60, 30)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout.addWidget(button, 1, 1, 1, 1)

        button = QPushButton("Button5")
        button.setMinimumSize(60, 30)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 列扩展，定位在第2行第1列位置，占1行2列
        self.layout.addWidget(button, 2, 0, 1, 2)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
