# @Time :2022/11/3 11:45
# @Author : Jerry Y
# @File  : QTreeWidget控件.py
# @Info  : 树形单元


'''
QTreeWidget树形单元组件继承自QTreeView类，可以用来来创建简单地树形结构列表。通过QTreeWidget类和QTreeWidgetItem类实现树形结构，
QTreeWidgetItem类实现结点的添加。
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.treeWidget = QTreeWidget(self)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.treeWidget)
        self.setLayout(self.layout)

    def initUI(self):
        root = self.treeWidget.invisibleRootItem()
        for row in range(4):
            item = QTreeWidgetItem()
            item.setData(0, Qt.DisplayRole, row)
            root.addChild(item)
            # 设置数据项显示数据角色的数据
            root.addChild(item)
            for column in range(3):
                child = QTreeWidgetItem()
                child.setData(0, Qt.DisplayRole, column)
                item.addChild(child)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
