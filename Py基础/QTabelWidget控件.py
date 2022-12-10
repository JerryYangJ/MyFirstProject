# @Time :2022/11/3 11:42
# @Author : Jerry Y
# @File  : QTabelWidget控件.py
# @Info  : 表格单元


'''
QTableWidget表格单元组件继承自QTableView，QTableView可以使用自定义的数据模型来显示内容，而QTableWidget则只能使用标准的数据模型，并且其单
元格数据是QTableWidgetItem的对象来实现的，QTableWidgetItem用来表示表格中的一个单元格，整个表格都需要用逐个单元格构建起来。

方法：
    setSpan(int, int, int, int)     四个参数分别代表，起始行，列，合并的行数，全并的列数，合并的内容为起始行列的内容
    clearSpans()                    清除所有合并的单元格

'''
'''
QTableWidget表格单元组件继承自QTableView，QTableView可以使用自定义的数据模型来显示内容，而QTableWidget则只能使用标准的数据模型，并且其单
元格数据是QTableWidgetItem的对象来实现的，QTableWidgetItem用来表示表格中的一个单元格，整个表格都需要用逐个单元格构建起来。

方法：
    setSpan(int, int, int, int)     四个参数分别代表，起始行，列，合并的行数，全并的列数，合并的内容为起始行列的内容
    clearSpans()                    清除所有合并的单元格

QTableWidgetItem的构造方法有4个：
    QTableWidgetItem(int type = Type)：构建一个空项
    QTableWidgetItem(str text,int type = Type)：构建一个带文本的项
    QTableWidgetItem(QIcon icon, str text, int type = Type) ：构建一个带图标和文本的项
    QTableWidgetItem(QTableWidgetItem other)：从other复制项的内容构建一个新项

表头及属性
    -“列1”、“列2”、“列3”为横表头，横表头可通过方法setHorizontalHeaderLabels来设置
    -“行1”、“行2”、“行3”为竖表头。，竖表头可以通过setVerticalHeaderLabels来设置。

QTableWidget允许多种数据类型的设置，理论上来说只要是QVariant能够接受的类型，都可以作为表格的内容来呈现。一般的文字信息采用setText()来设置，
而如果是其他类型，比如int，则需要使用setData()来设置。注意，这两个函数都是QTableWidgetItem提供的。如果没有前导0这样的特殊需求，
推荐使用setData()而不是setText(QString::number())的方式来设置数值，因为这样将导致数字类型的数据在排序时出现10比2优先的情况。

QTableWidget部件中的QTableWidgetItem项数据可以通过项的data( int role) 方法获取项中指定列指定角色的数据，也可以通过
setData(int role, QVariant value)方法设置指定角色的数据为value。例如项的文本可以通过data方法和setData方法使用Qt.DisplayRole、
Qt.EditRole这两种角色去访问。
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tableWidget = QTableWidget(self)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def initUI(self):
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        for row in range(10):
            for column in range(5):
                item = QTableWidgetItem()
                # 设置数据项显示数据角色的数据
                item.setData(Qt.DisplayRole, column)
                self.tableWidget.setItem(row, column, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())