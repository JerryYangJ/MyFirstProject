# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QMS检验记录与生产订单匹配检查.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog


class Ui_QMS(object):
    def setupUi(self, QMS):
        QMS.setObjectName("QMS")
        QMS.resize(534, 524)
        self.widget = QtWidgets.QWidget(QMS)
        self.widget.setGeometry(QtCore.QRect(10, 20, 511, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PushButton = QtWidgets.QPushButton(self.widget)
        self.PushButton.setObjectName("PushButton")
        self.gridLayout.addWidget(self.PushButton, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.PushButton_2 = QtWidgets.QPushButton(self.widget)
        self.PushButton_2.setObjectName("PushButton_2")
        self.gridLayout.addWidget(self.PushButton_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.PushButton_3 = QtWidgets.QPushButton(self.widget)
        self.PushButton_3.setObjectName("PushButton_3")
        self.gridLayout.addWidget(self.PushButton_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.PushButton_4 = QtWidgets.QPushButton(self.widget)
        self.PushButton_4.setObjectName("PushButton_4")
        self.gridLayout.addWidget(self.PushButton_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.PushButton_5 = QtWidgets.QPushButton(self.widget)
        self.PushButton_5.setObjectName("PushButton_5")
        self.gridLayout.addWidget(self.PushButton_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.PushButton_6 = QtWidgets.QPushButton(self.widget)
        self.PushButton_6.setObjectName("PushButton_6")
        self.gridLayout.addWidget(self.PushButton_6, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.PushButton_7 = QtWidgets.QPushButton(self.widget)
        self.PushButton_7.setObjectName("PushButton_7")
        self.verticalLayout.addWidget(self.PushButton_7)

        self.retranslateUi(QMS)
        self.PushButton.clicked.connect(self.lineEdit_setText) # type: ignore
        self.PushButton_2.clicked.connect(self.lineEdit2_setText) # type: ignore
        self.PushButton_3.clicked.connect(self.lineEdit3_setText) # type: ignore
        self.PushButton_4.clicked.connect(self.lineEdit4_setText) # type: ignore
        self.PushButton_5.clicked.connect(self.lineEdit5_setText) # type: ignore
        self.PushButton_6.clicked.connect(self.lineEdit6_setText) # type: ignore
        self.PushButton_7.clicked.connect(self.get_rusalt) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QMS)

    def retranslateUi(self, QMS):
        _translate = QtCore.QCoreApplication.translate
        QMS.setWindowTitle(_translate("QMS", "Form"))
        self.PushButton.setText(_translate("QMS", "导入8010管材检验记录"))
        self.PushButton_2.setText(_translate("QMS", "导入8012检验记录"))
        self.PushButton_3.setText(_translate("QMS", "导入8010管件检验记录"))
        self.PushButton_4.setText(_translate("QMS", "导入管材订单记录"))
        self.PushButton_5.setText(_translate("QMS", "导入市政订单记录"))
        self.PushButton_6.setText(_translate("QMS", "导入管件订单记录"))
        self.label.setText(_translate("QMS", "执行结果："))
        self.PushButton_7.setText(_translate("QMS", "执行检查"))

    def get_rusalt(self):
        """执行拼接代码，并存储匹配文件"""

        # 获取文件
        data1_filename = self.lineEdit.text()
        data2_filename = self.lineEdit_2.text()
        data3_filename = self.lineEdit_3.text()
        data4_filename = self.lineEdit_4.text()
        data5_filename = self.lineEdit_5.text()
        data6_filename = self.lineEdit_6.text()
        print(data1_filename)
        print(data2_filename)
        print(data3_filename)
        print(data4_filename)
        print(data5_filename)


        # 读取管材检验单文件
        data1 = pd.read_excel(data1_filename, sheet_name='Sheet1')
        data2 = pd.read_excel(data2_filename, sheet_name='Sheet1')
        data_guanjian = pd.read_excel(data3_filename, sheet_name='Sheet1')
        # print(data1)

        # 选择管材检验单中的"批号”列,并合并
        se1 = data1['批号']
        se2 = data2['批号']
        se3 = data_guanjian['生产订单号']

        se_pihao = pd.concat([se1, se2]).reset_index(drop=True)
        # print(se_pihao)
        # 删除重复项
        se_pihao = se_pihao.drop_duplicates(keep='last')
        se3 = se3.drop_duplicates(keep='last')
        # 将”批号“中的”_"删除
        se_pihao = se_pihao.str.replace('_', '')
        # print(se_pihao)
        # 将series转成DF1024
        df = pd.DataFrame(se_pihao, columns=['批号'])
        df['是否检测'] = se_pihao
        df_guanjian = pd.DataFrame(se3, columns=['生产订单号'])
        df_guanjian['是否检测'] = se3
        # print(df_guanjian)

        data3 = pd.read_excel(data4_filename, sheet_name='管材8010')
        data3 = data3.loc[:, ['生产工厂', '产品类别', '批号']]
        data4 = pd.read_excel(data4_filename, sheet_name='管材8012')
        data4 = data4.loc[:, ['生产工厂', '产品类别', '批号']]
        data5 = pd.read_excel(data5_filename, sheet_name='管材')
        data5 = data5.loc[:, ['生产工厂', '产品类别', '批号']]
        data6 = pd.read_excel(data6_filename, sheet_name='管件')
        data6 = data6.loc[:, ['机台', '生产订单号']]
        print(data6)
        # 合并8010、8012两个表
        table_merge = pd.concat([data3, data4, data5]).reset_index(drop=True)

        # 拼接表格
        table = table_merge.merge(df, how='left', on='批号').fillna(0)
        count_8010_1 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8010)].loc[table['产品类别'].apply(lambda x: x == '管材')][
            '是否检测'].count()
        # print("8010管材订单总数为：", count_8010_1)
        count_8012_1 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '管材')][
            '是否检测'].count()
        # print("8012管材订单总数为：", count_8012_1)
        count_8012_2 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '市政')][
            '是否检测'].count()
        # print("8012市政订单总数为：", count_8012_2)

        table2 = data6.merge(df_guanjian, how='left', on='生产订单号').fillna(0)
        # print(table2)

        # 将文件写入文件
        writer = pd.ExcelWriter('结果.xlsx', engine='openpyxl')
        table.to_excel(writer, sheet_name='Sheet1')
        table2.to_excel(writer, sheet_name='Sheet2')
        writer.save()
        # t = table.groupby(['是否检测']).count()
        t_8010_1 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8010)].loc[table['产品类别'].apply(lambda x: x == '管材')].loc[
            table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
        print("8010管材订单总数为：", count_8010_1, '\t', "未检测订单总数为：", t_8010_1)
        t_8012_1 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '管材')].loc[
            table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
        print("8012管材订单总数为：", count_8012_1, '\t', "未检测订单总数为：", t_8012_1)
        t_8012_2 = \
        table.loc[table['生产工厂'].apply(lambda x: x == 8012)].loc[table['产品类别'].apply(lambda x: x == '市政')].loc[
            table['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
        print("8012市政订单总数为：", count_8012_2, '\t', "未检测订单总数为：", t_8012_2)

        # 管件
        t_8010_guanjian = table2.loc[table2['是否检测'].apply(lambda x: x == 0)]['是否检测'].count()
        count_8010_guanjian = table2['是否检测'].count()
        print("8010管件订单总数为：", count_8010_guanjian, '\t', "未检测订单总数为：", t_8010_guanjian)

        # 将结果输出在label上
        # self.label.setText(f"8010管材订单总数为：{count_8010_1}"+ '\t'+ f"未检测订单总数为：{t_8010_1}"+"\n"+f"8012管材订单总数为：{count_8012_1}"+'\t'+f"未检测订单总数为：{t_8012_1}"+"\n"+f"8012市政订单总数为：{count_8012_2}"+ '\t'+f"未检测订单总数为：{t_8012_2}"+"\n"+f"8010管件订单总数为：{count_8010_guanjian}"+'\t'+f"未检测订单总数为：{t_8010_guanjian}")
        # print(f"8010管材订单总数为：{count_8010_1}"+ '\t'+ f"未检测订单总数为：{t_8010_1}"+"\n"+f"8012管材订单总数为：{count_8012_1}"+'\t'+f"未检测订单总数为：{t_8012_1}"+"\n"+f"8012市政订单总数为：{count_8012_2}"+ '\t'+f"未检测订单总数为：{t_8012_2}"+"\n"+f"8010管件订单总数为：{count_8010_guanjian}"+'\t'+f"未检测订单总数为：{t_8010_guanjian}")

    def lineEdit_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit.setText(file)

    def lineEdit2_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit_2.setText(file)

    def lineEdit3_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit_3.setText(file)

    def lineEdit4_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit_4.setText(file)

    def lineEdit5_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit_5.setText(file)

    def lineEdit6_setText(self):
        # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/")  # 返回文件路径和文件类型，分别接收，默认为All Files
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:\pythonProject\pandas\拼接")   # Text File (*.txt)为文件过滤器
        # print(file, type)
        self.lineEdit_6.setText(file)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)

    # 方法一：使用PyUIC5工具将ui文件转为代码
    # myWin = QMainWindow()
    myWin = QWidget()
    myUI = Ui_QMS()
    myUI.setupUi(myWin)
    myWin.show()
    sys.exit(myApp.exec_())