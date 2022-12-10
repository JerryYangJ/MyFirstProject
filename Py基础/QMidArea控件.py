# @Time :2022/11/3 11:52
# @Author : Jerry Y
# @File  : QMidArea控件.py
# @Info  : 多文档界面

'''
QMdiArea组件是一种多文档界面，MDI即Multiple Document Interface，主要适用于完成一项工作时需要用到多个文件。
QMainWindow是SDI（Signal Document Interface，单文档界面），每个开启的文件占据一个视窗，主要适用于没有太多文件的应用场景。
QMdiSubWindow类继承自QWidget，主要用来创建MDI子窗体实例。
'''

import sys
from PyQt5.QtWidgets import QApplication, QMdiArea, QMdiSubWindow


class MainWindow(QMdiArea):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.addSubWindow(QMdiSubWindow())
        self.addSubWindow(QMdiSubWindow())
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
