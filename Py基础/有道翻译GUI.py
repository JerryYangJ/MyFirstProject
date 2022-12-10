# @Time :2022/11/28 15:23
# @Author : Jerry Y
# @File  : 有道翻译GUI.py
# @Info  :
import random
import sys
import time
from hashlib import md5

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 341, 221))
        # 设置label对齐方式
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(lambda: self.translate(self.lineEdit.text()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "翻译"))

    def get_translate_result(self, word):
        headers = {
            # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '255',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1427037532@10.112.57.87; OUTFOX_SEARCH_USER_ID_NCOO=1593359534.2085323; ___rl__test__cookies=1669601697352',
            # 'Host': 'fanyi.youdao.com',
            # 'Origin': 'https://fanyi.youdao.com',
            'Referer': 'https://fanyi.youdao.com/',
            # 'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': '"Windows"',
            # 'Sec-Fetch-Dest': 'empty',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
            # 'X-Requested-With': 'XMLHttpRequest'
        }
        # word = input("请输入您要翻译的词语：")
        lts = int(time.time() * 100)
        salt = str(lts) + str(random.randint(0, 9))
        sign = md5(str("fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5").encode("utf-8")).hexdigest()

        data_dic = {
            'i': word,  # 'stop'
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,  # '16696029066810'
            'sign': sign,  # 'f567b016bcb5282b469fdc479417e606'
            'lts': lts,  # '1669602906681'
            'bv': '9397f26bba9ce788f6f7b6587fede389',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

        url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

        res = requests.post(url=url, headers=headers, data=data_dic)
        # print(res.text)
        translateResult = res.json()['translateResult'][0][0]['tgt']
        print(translateResult)
        return translateResult

    def translate(self, word):
        self.label.setText(self.get_translate_result(word))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(win)
    win.show()

    sys.exit(app.exec_())
