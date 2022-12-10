# @Time :2022/11/3 11:33
# @Author : Jerry Y
# @File  : QTableView控件_test.py
# @Info  : 表格视图

'''
QTableView可以使用自定义的数据模型来显示内容，通过setModel绑定数据源，由QAbstractItemView类定义的接口来实现，
使其能够显示由QAbstractItemModel类派生的模型提供的数据。

标准模型
    QStringListModel 字符串链表数据模型
    QStandardItemModel标准数据项模型，存储任意结构层次的数据
    QDirModel 文件系统目录模型
    QSqlQueryModel SQL查询结果集数据模型
    QSqlTableModel SQL表格数据模型
    QSqlRelationTableModel 关系型SQL表格数据模型
    QSortFilterProxyModel 排序过滤代理模型

'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QStandardItemModel(4, 4)
        headers = ["序号", "姓名", "工号", "岗位"]
        self.model.setHorizontalHeaderLabels(headers)
        self.tableView = QTableView(self)
        # 最后一列拉伸
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 设置模型
        self.tableView.setModel(self.model)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.tableView)
        self.setLayout(self.layout)

    def initUI(self):
        '''
        # 数据项增加
        for row in range(10):
            for column in range(4):
                item = QStandardItem()  # 创建item对象
                item.setText(str(column))   # 在item对象中加入要显示的内容
                self.model.setItem(row, column, item) # 将item对象加入model模型
        # 增加一行
        for row in range(5):
            items = []
            for column in range(4):
                items.append(QStandardItem(str(column)))
            self.model.appendRow(items)
        '''
        for row in range(4):
            for column in range(4):
                item = QStandardItem()
                item.setText(f'第{row+1}行第{column+1}列')
                self.model.setItem(row, column, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(1024, 800)
    window.show()

    sys.exit(app.exec_())
