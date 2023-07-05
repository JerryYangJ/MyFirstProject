# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edgeTTS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1103, 629)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 781, 601))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.file_select_Button = QtWidgets.QPushButton(self.tab_2)
        self.file_select_Button.setGeometry(QtCore.QRect(20, 30, 116, 23))
        self.file_select_Button.setObjectName("file_select_Button")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(141, 30, 621, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.do_Button = QtWidgets.QPushButton(Form)
        self.do_Button.setEnabled(True)
        self.do_Button.setGeometry(QtCore.QRect(820, 450, 251, 51))
        self.do_Button.setObjectName("do_Button")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(811, 21, 261, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.language = QtWidgets.QLabel(self.layoutWidget)
        self.language.setObjectName("language")
        self.verticalLayout.addWidget(self.language)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.speaker_name = QtWidgets.QLabel(self.layoutWidget)
        self.speaker_name.setObjectName("speaker_name")
        self.verticalLayout.addWidget(self.speaker_name)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rate_show = QtWidgets.QLabel(self.layoutWidget)
        self.rate_show.setAutoFillBackground(True)
        self.rate_show.setObjectName("rate_show")
        self.horizontalLayout.addWidget(self.rate_show)
        self.rate = QtWidgets.QLabel(self.layoutWidget)
        self.rate.setAutoFillBackground(True)
        self.rate.setObjectName("rate")
        self.horizontalLayout.addWidget(self.rate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setMinimum(-200)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.test_Button = QtWidgets.QPushButton(Form)
        self.test_Button.setGeometry(QtCore.QRect(820, 510, 251, 51))
        self.test_Button.setObjectName("test_Button")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider.valueChanged['int'].connect(self.rate.setNum) # type: ignore
        self.comboBox.currentTextChanged['QString'].connect(self.comboBox_2.setEditText) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "微软文字转语音"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "文本转换"))
        self.file_select_Button.setText(_translate("Form", "选择需要转换的文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "文件转换"))
        self.do_Button.setText(_translate("Form", "开始"))
        self.language.setText(_translate("Form", "语言"))
        self.speaker_name.setText(_translate("Form", "语音"))
        self.rate_show.setText(_translate("Form", "语速"))
        self.rate.setText(_translate("Form", "0"))
        self.test_Button.setText(_translate("Form", "试听"))