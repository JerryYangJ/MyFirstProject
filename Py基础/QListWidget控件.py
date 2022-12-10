# @Time :2022/11/3 11:46
# @Author : Jerry Y
# @File  : QListWidget控件.py
# @Info  : 列表单元

'''
QListWidget列表单元组件继承自QListView，可以显示一个列表，列表中的每个项是QListWidgetItem的一个实例，每个项可以通过QListWidgetItem
来操作。可以通过QListWidgetItem来设置每个项的图像与文字。
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.listWidget = QListWidget(self)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)

    def initUI(self):
        for i in range(10):
            item = QListWidgetItem()
            # 设置数据项显示数据角色的数据
            item.setData(Qt.DisplayRole, i)
            self.listWidget.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
