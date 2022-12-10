# @Time :2022/11/3 11:42
# @Author : Jerry Y
# @File  : QTabelWidget控件_text.py
# @Info  : 使用pymysql链接数据库，查询数据，使用QTabelWidget控件显示数据。




import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from pymysql import *


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
        # for row in range(10):
        #     for column in range(5):
        #         item = QTableWidgetItem()
        #         # 设置数据项显示数据角色的数据
        #         item.setData(Qt.DisplayRole, column)
        #         self.tableWidget.setItem(row, column, item)
        data, count = self.getData()

        # 按data数据行数，调整tableWidget的行数
        self.tableWidget.setRowCount(count)

        for i, row in enumerate(data):  # enumerate，给遍历的数据对象添加索引
            print(i, row)
            # # 方法1：
            # item = QTableWidgetItem()
            # item_1 = QTableWidgetItem()
            # item.setData(Qt.DisplayRole, row[0])
            # item_1.setData(Qt.DisplayRole, row[1])
            # self.tableWidget.setItem(i, 0, item)
            # self.tableWidget.setItem(i, 1, item_1)

            # 方法2：

            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row[1]))

    def getData(self):
        # 创建Connection
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='jerry123',
                       charset='utf8')
        # 获取Cursor对象（游标）
        cs1 = conn.cursor()

        # # 查询数据
        # count = cs1.execute('select id,name from goods where id>=4')
        count = cs1.execute('select id,name from goods')
        # print(count)
        # print(cs1.fetchall())

        # 关闭Cursor对象
        cs1.close()
        # 关闭Connection对象
        conn.close()

        return cs1.fetchall(), count


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.initUI()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
