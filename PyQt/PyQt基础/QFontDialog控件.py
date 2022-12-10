# @Time :2022/10/28 14:04
# @Author : Jerry Y
# @File  : QFontDialog控件.py
# @Info  : 字体对话框


'''



'''


import sys
from PyQt5 import QtWidgets, QtCore


class FontDialog(QtWidgets.QWidget):
    def __init__(self):
        super(FontDialog, self).__init__()

        self.setWindowTitle("字体对话框示例程序")
        self.setGeometry(300, 300, 250, 110)

        self.button = QtWidgets.QPushButton("对话框", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)

        self.label = QtWidgets.QLabel("普通的disco我们普通的摇", self)
        self.label.move(130, 30)

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.button)
        # 将label标签加入到hbox布局中，并通过第二个参数1设置label的大小是可变的。该设置是必须的，因为在用户选择不同的字体时，label标签中的字体可能会变大，若不进行该设置，标签中的内容就可能不会被全部显示。
        self.h_box.addWidget(self.label, 1)
        self.setLayout(self.h_box)

    def show_dialog(self):
        # 弹出对话框
        font, ok = QtWidgets.QFontDialog.getFont(self)  # 返回字体对象和一个bool选项
        print(font, ok)
        if ok:
            self.label.setFont(font)

app = QtWidgets.QApplication(sys.argv)
fd = FontDialog()
fd.show()
sys.exit(app.exec_())


