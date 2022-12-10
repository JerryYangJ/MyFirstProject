# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt实战：人员管理系统.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("人员管理系统")
        Form.resize(940, 716)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 240, 901, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '身份证', '专业', '电话', '部门', '地址', '职务', '出生日期', '备注'])
        self.widget = QtWidgets.QWidget(Form)
        # 改为选择一行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 禁用双击编辑单元格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 添加右击菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generate_menu)
        # 设置大小、位置
        self.widget.setGeometry(QtCore.QRect(20, 10, 901, 161))

        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_gender = QtWidgets.QLabel(self.widget)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.gridLayout.addWidget(self.label_gender, 0, 2, 1, 1)
        # self.lineEdit_gender = QtWidgets.QLineEdit(self.widget)
        # self.lineEdit_gender.setFont(font)
        # self.lineEdit_gender.setObjectName("lineEdit_gender")
        self.comboBox_gender = QtWidgets.QComboBox(self.widget)
        self.comboBox_gender.setFont(font)
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("男")
        self.comboBox_gender.addItem("女")
        self.gridLayout.addWidget(self.comboBox_gender, 0, 3, 1, 1)
        self.label_id = QtWidgets.QLabel(self.widget)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 0, 4, 1, 1)
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.gridLayout.addWidget(self.lineEdit_id, 0, 5, 1, 1)
        self.label_skill = QtWidgets.QLabel(self.widget)
        self.label_skill.setFont(font)
        self.label_skill.setObjectName("label_skill")
        self.gridLayout.addWidget(self.label_skill, 1, 0, 1, 1)
        self.lineEdit_skill = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_skill.setFont(font)
        self.lineEdit_skill.setObjectName("lineEdit_skill")
        self.gridLayout.addWidget(self.lineEdit_skill, 1, 1, 1, 1)
        self.label_phone = QtWidgets.QLabel(self.widget)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout.addWidget(self.label_phone, 1, 2, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout.addWidget(self.lineEdit_phone, 1, 3, 1, 1)
        self.label_department = QtWidgets.QLabel(self.widget)
        self.label_department.setFont(font)
        self.label_department.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_department.setObjectName("label_department")
        self.gridLayout.addWidget(self.label_department, 1, 4, 1, 1)
        self.lineEdit_department = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_department.setFont(font)
        self.lineEdit_department.setObjectName("lineEdit_department")
        self.gridLayout.addWidget(self.lineEdit_department, 1, 5, 1, 1)
        self.label_addr = QtWidgets.QLabel(self.widget)
        self.label_addr.setFont(font)
        self.label_addr.setObjectName("label_addr")
        self.gridLayout.addWidget(self.label_addr, 2, 0, 1, 1)
        self.lineEdit_addr = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_addr.setFont(font)
        self.lineEdit_addr.setObjectName("lineEdit_addr")
        self.gridLayout.addWidget(self.lineEdit_addr, 2, 1, 1, 1)
        self.label_post = QtWidgets.QLabel(self.widget)
        self.label_post.setFont(font)
        self.label_post.setObjectName("label_post")
        self.gridLayout.addWidget(self.label_post, 2, 2, 1, 1)
        self.lineEdit_post = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_post.setFont(font)
        self.lineEdit_post.setObjectName("lineEdit_post")
        self.gridLayout.addWidget(self.lineEdit_post, 2, 3, 1, 1)
        self.label_birthdate = QtWidgets.QLabel(self.widget)
        self.label_birthdate.setFont(font)
        self.label_birthdate.setObjectName("label_birthdate")
        self.gridLayout.addWidget(self.label_birthdate, 2, 4, 1, 1)
        self.dateEdit_birthdate = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_birthdate.setFont(font)
        self.dateEdit_birthdate.setObjectName("dateEdit_birthdate")
        self.gridLayout.addWidget(self.dateEdit_birthdate, 2, 5, 1, 1)
        self.label_note = QtWidgets.QLabel(self.widget)
        self.label_note.setFont(font)
        self.label_note.setObjectName("label_note")
        self.gridLayout.addWidget(self.label_note, 3, 0, 1, 1)
        self.textEdit_note = QtWidgets.QTextEdit(self.widget)
        self.textEdit_note.setFont(font)
        self.textEdit_note.setObjectName("textEdit_note")
        self.gridLayout.addWidget(self.textEdit_note, 3, 1, 2, 3)
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 3, 4, 2, 1)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 200, 901, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_showall = QtWidgets.QPushButton(self.widget1)
        self.pushButton_showall.setFont(font)
        self.pushButton_showall.setObjectName("pushButton_showall")
        self.horizontalLayout.addWidget(self.pushButton_showall)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['姓名', '性别', '身份证', '专业', '电话', '部门', '地址', '职务', '出生日期', '备注'])
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout.addWidget(self.lineEdit_9)
        self.pushButton_find = QtWidgets.QPushButton(self.widget1)
        self.pushButton_find.setFont(font)
        self.pushButton_find.setObjectName("pushButton_find")
        self.horizontalLayout.addWidget(self.pushButton_find)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_add.clicked.connect(lambda: self.add(Form))
        self.pushButton_showall.clicked.connect(self.showAll)
        self.pushButton_find.clicked.connect(lambda: self.find(Form))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "姓名："))
        self.label_gender.setText(_translate("Form", "性别："))
        self.label_id.setText(_translate("Form", "身份证："))
        self.label_skill.setText(_translate("Form", "专业："))
        self.label_phone.setText(_translate("Form", "电话："))
        self.label_department.setText(_translate("Form", "部门："))
        self.label_addr.setText(_translate("Form", "地址："))
        self.label_post.setText(_translate("Form", "职务："))
        self.label_birthdate.setText(_translate("Form", "出生日期"))
        self.label_note.setText(_translate("Form", "备注："))
        self.pushButton_add.setText(_translate("Form", "录入信息"))
        self.pushButton_showall.setText(_translate("Form", "查看全部"))
        self.label.setText(_translate("Form", "按类型查找："))
        self.pushButton_find.setText(_translate("Form", "查找"))

    def generate_menu(self):
        '''右键菜单'''
        pass

    def add(self, Form):
        name = self.lineEdit_name.text()
        gender = self.comboBox_gender.currentText()  # 获取comboBox的值
        ids = self.lineEdit_id.text()
        skill = self.lineEdit_skill.text()
        phone = self.lineEdit_phone.text()
        department = self.lineEdit_department.text()
        addr = self.lineEdit_addr.text()
        post = self.lineEdit_post.text()
        birthday = self.dateEdit_birthdate.text()
        note = self.textEdit_note.toPlainText()
        infoList = [name, gender, ids, skill, phone, department, addr, post, birthday, note]
        print(infoList)
        if '' in infoList[:-1]:  # 除备注信息，其他信息不允许为空
            QMessageBox.information(Form, '提示', '输入的信息不能为空')
        else:
            info_str = ','.join(infoList)
            with open('infos.txt', 'a+', encoding='utf-8') as f:
                f.write(info_str + '\n')
            self.showAll()
            QMessageBox.information(Form, "提示", "提交成功")

    def showAll(self):
        with open('infos.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.tableWidget.setRowCount(len(lines))

        for i, line in enumerate(lines):
            for n, col in enumerate(line.split(',')):
                self.tableWidget.setItem(i, n, QTableWidgetItem(col))
                # print(i, n, col)
                self.tableWidget.setItem(i, n, QTableWidgetItem(col))

    def find(self, Form):
        find_type = self.comboBox.currentText()
        find_word = self.lineEdit_9.text()
        row_n = 0
        # 初始化表格
        self.tableWidget.setRowCount(row_n)
        with open('infos.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if find_word:
                if find_type == '姓名':
                    self.tableWidget.setRowCount(1)
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[0]:
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            break
                    else:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '性别':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[1]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '身份证':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[2]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '专业':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[3]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '电话':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[4]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '部门':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[4]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '地址':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[5]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '职务':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[6]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '出生日期':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[7]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
                elif find_type == '备注':
                    for line in lines:
                        line_list = line.split(',')
                        if find_word in line_list[8]:
                            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                            for col_n, col in enumerate(line_list):
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                                self.tableWidget.setItem(row_n, col_n, QTableWidgetItem(col))
                            row_n += 1
                    if row_n == 0:
                        QMessageBox.information(Form, "提示", f"您要查找的“{find_type}”包含“{find_word}”不存在")
            else:
                QMessageBox.information(Form, '提示', '输入的查询信息为空')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
