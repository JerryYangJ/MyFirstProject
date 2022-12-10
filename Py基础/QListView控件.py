# @Time :2022/11/3 11:41
# @Author : Jerry Y
# @File  : QListView控件.py
# @Info  : 列表视图

'''
QListView是列表视图，继承自QAbstractItemView，不显示表头和表框，为Qt的Model/View结构提供了更灵活的方式。

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel,QStandardItem


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QStandardItemModel()
        self.listView = QListView(self)
        self.listView.setModel(self.model)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listView)
        self.setLayout(self.layout)

    def initUI(self):
        root = self.model.invisibleRootItem()
        for i in range(10):
            item = QStandardItem(str(i))
            root.setChild(i, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
