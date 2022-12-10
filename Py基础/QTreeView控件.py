# @Time :2022/11/3 11:40
# @Author : Jerry Y
# @File  : QTreeView控件.py
# @Info  : 树形结构的视图

'''
QTreeView是一种树形结构的视图，继承自QAbstractItemView，是Model/View框架的一部分。

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel,QStandardItem


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QStandardItemModel()
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.model)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.treeView)
        self.setLayout(self.layout)

    def initUI(self):
        root = self.model.invisibleRootItem()
        for i in range(4):
            item = QStandardItem(str(i))
            for j in range(3):
                chidItem = QStandardItem(str(j))
                item.setChild(j, chidItem)
            root.setChild(i, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
