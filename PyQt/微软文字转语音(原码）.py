import sys
import os

import edge_tts
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog, QSlider

en_speaker_name_listName = [
    'en-AU-NatashaNeural',
    'en-AU-WilliamNeural',
    'en-CA-ClaraNeural',
    'en-CA-LiamNeural',
    'en-GB-LibbyNeural',
    'en-GB-MaisieNeural',
    'en-GB-RyanNeural',
    'en-GB-SoniaNeural',
    'en-GB-ThomasNeural',
    'en-HK-SamNeural',
    'en-HK-YanNeural',
    'en-IE-ConnorNeural',
    'en-IE-EmilyNeural',
    'en-IN-NeerjaExpressiveNeural',
    'en-IN-NeerjaNeural',
    'en-IN-PrabhatNeural',
    'en-KE-AsiliaNeural',
    'en-KE-ChilembaNeural',
    'en-NG-AbeoNeural',
    'en-NG-EzinneNeural',
    'en-NZ-MitchellNeural',
    'en-NZ-MollyNeural',
    'en-PH-JamesNeural',
    'en-PH-RosaNeural',
    'en-SG-LunaNeural',
    'en-SG-WayneNeural',
    'en-TZ-ElimuNeural',
    'en-TZ-ImaniNeural',
    'en-US-AnaNeural',
    'en-US-AriaNeural',
    'en-US-ChristopherNeural',
    'en-US-EricNeural',
    'en-US-GuyNeural',
    'en-US-JennyNeural',
    'en-US-MichelleNeural',
    'en-US-RogerNeural',
    'en-US-SteffanNeural',
    'en-ZA-LeahNeural',
    'en-ZA-LukeNeural'
]
zh_speaker_name_listName = [
    'zh-CN-XiaoxiaoNeural',
    'zh-CN-XiaoyiNeural',
    'zh-CN-YunjianNeural',
    'zh-CN-YunxiNeural',
    'zh-CN-YunxiaNeural',
    'zh-CN-YunyangNeural',
    'zh-CN-liaoning-XiaobeiNeural',
    'zh-CN-shaanxi-XiaoniNeural',
    'zh-HK-HiuGaaiNeural',
    'zh-HK-HiuMaanNeural',
    'zh-HK-WanLungNeural',
    'zh-TW-HsiaoChenNeural',
    'zh-TW-HsiaoYuNeural',
    'zh-TW-YunJheNeural'
]


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
        self.file_select_Button.setGeometry(QtCore.QRect(20, 30, 180, 30))
        self.file_select_Button.setObjectName("file_select_Button")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 550, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.do_Button = QtWidgets.QPushButton(Form)
        self.do_Button.setGeometry(QtCore.QRect(820, 550, 251, 51))
        self.do_Button.setObjectName("do_Button")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(811, 21, 261, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.language = QtWidgets.QLabel(self.widget)
        self.language.setObjectName("language")
        self.verticalLayout.addWidget(self.language)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("中文")
        self.comboBox.addItem("英文")

        self.verticalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.speaker_name = QtWidgets.QLabel(self.widget)
        self.speaker_name.setObjectName("speaker_name")
        self.verticalLayout.addWidget(self.speaker_name)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        for zh_speaker_name in zh_speaker_name_listName:
            self.comboBox_2.addItem(zh_speaker_name)

        self.verticalLayout.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rate_show = QtWidgets.QLabel(self.widget)
        self.rate_show.setAutoFillBackground(True)
        self.rate_show.setObjectName("rate_show")
        self.horizontalLayout.addWidget(self.rate_show)
        self.rate = QtWidgets.QLabel(self.widget)
        self.rate.setAutoFillBackground(True)
        self.rate.setObjectName("rate")
        self.horizontalLayout.addWidget(self.rate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setMinimum(-200)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setSingleStep(10)
        # self.horizontalSlider.setPageStep(40)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setTickInterval(40)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout.addWidget(self.horizontalSlider)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider.valueChanged['int'].connect(self.rate.setNum)  # type: ignore
        self.comboBox.currentIndexChanged.connect(self.comboBox_2_setEditText)  # type: ignore
        self.do_Button.clicked.connect(self.do_Button_click)    # type: ignore
        self.file_select_Button.clicked.connect(self.lineEdit_setText)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "微软文字转语音v1    制作：Jerry Yang"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "文本转换"))
        self.file_select_Button.setText(_translate("Form", "选择需要转换的文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "文件转换"))
        self.do_Button.setText(_translate("Form", "开始"))
        self.language.setText(_translate("Form", "语言"))
        self.speaker_name.setText(_translate("Form", "语音"))
        self.rate_show.setText(_translate("Form", "语速"))
        self.rate.setText(_translate("Form", "0"))

    def comboBox_2_setEditText(self):
        """设置comboBox_2的选择项 """

        # 清空comboBox_2的Item选项
        self.comboBox_2.clear()

        # 根据comboBox选择项载入comboBox_2的选择项
        if self.comboBox.currentText() == "中文":
            for zh_speaker_name in zh_speaker_name_listName:
                self.comboBox_2.addItem(zh_speaker_name)
        elif self.comboBox.currentText() == "英文":
            for en_speaker_name in en_speaker_name_listName:
                self.comboBox_2.addItem(en_speaker_name)

    def do_Button_click(self):
        """ 开始按钮的槽函数 """
        # 获取程序执行路径
        currPath = sys.path[0]
        highPath = os.path.split(currPath)
        print("程序执行路径:", currPath)

        # 判断tabWidget在哪个Index
        if self.tabWidget.currentIndex() == 0:
            text = self.textEdit.toPlainText()
            text = text.replace('\n', '。')
            print(text)
            rate = self.horizontalSlider.value()
            if rate == 0:
                os.system(f'edge-tts --text {text} --write-media "d:/111.mp3" --voice {self.comboBox_2.currentText()}')
            else:
                if rate > 0:
                    rate = '+' + str(rate) + '%'
                elif rate < 0:
                    rate = str(rate) + '%'
                os.system(
                    f'edge-tts --text {text} --write-media "d:/111.mp3" --voice {self.comboBox_2.currentText()} --rate={rate}')
        elif self.tabWidget.currentIndex() == 1:


            # 获取linEdit的文件路径
            path = self.lineEdit.text()
            print(path)

            # 文件保存path
            save_path = path.split(".")[0] + '.mp3'
            print(save_path)

            # 读取文件内容
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read().replace('\n', '。')
                print(text)
            # 获取语速，并根据语速调用edge_tts生成语音并保存
            rate = self.horizontalSlider.value()
            if rate == 0:
                os.system(f'{highPath[0]}+/dge-tts --text {text} --write-media {save_path} --voice {self.comboBox_2.currentText()}')
            else:
                if rate > 0:
                    rate = '+' + str(rate) + '%'
                elif rate < 0:
                    rate = str(rate) + '%'
                os.system(
                    f'edge-tts --text {text} --write-media {save_path}  --voice {self.comboBox_2.currentText()} --rate={rate}')

        # 调用edge-tts将textEdit的文字转换成语音保存
        # os.system(f'edge-tts --text {text} --write-media "d:/3.mp3" --voice {self.comboBox_2.currentText()} --rate={rate}')
        # COMMAND = f'edge-tts --text "今天天气真好，花儿对我笑" --write-media "d:/1.mp3" --voice zh-CN-YunxiNeural'
        # subprocess.run(COMMAND, shell=True)
        QMessageBox.information(myWin, "这是消息对话框标题", "已完成文字转语音")

    def lineEdit_setText(self):
        """显示文件path"""
        file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/",
                                                 'Text File (*.txt)')  # 返回文件路径和文件类型，分别接收，默认为All Files
        self.lineEdit.setText(file)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)

    myWin = QWidget()

    myUI = Ui_Form()
    myUI.setupUi(myWin)

    myWin.show()
    sys.exit(myApp.exec_())
