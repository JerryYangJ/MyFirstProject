# @Time :2022/11/3 11:51
# @Author : Jerry Y
# @File  : QDockWidget控件.py
# @Info  : 停靠窗体

'''
QDockWidget是停靠窗体组件，可以作为一个顶层窗口漂浮在桌面，主要作为辅助窗体出现在界面中。QDockWidget包含工具栏和内容区域，工具栏用于显示窗口
标题，一个浮动按钮和一个关闭按钮。QDockWidget可以作为子窗口部件的封装，通过setWidget()设置子窗口部件。

'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # central widget
        self.centralWidget = QTextEdit()
        self.centralWidget.setText("Main Window")
        self.centralWidget.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.centralWidget)
        # left dock
        dock = QDockWidget("Window1", self)
        dock.setFeatures(QDockWidget.DockWidgetMovable)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        textEdit = QTextEdit()
        textEdit.setText("Window1,The dock widget can be moved between docks and users")
        dock.setWidget(textEdit)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        # right dock
        dock =QDockWidget("Window2", self)
        dock.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable)
        textEdit =QTextEdit()
        textEdit.setText("Window2,The dock widget can be detac from the main window,""and float as an independent window,and can be closed")
        dock.setWidget(textEdit)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        # right dock
        dock =QDockWidget("Window3", self)
        dock.setFeatures(QDockWidget.AllDockWidgetFeatures)
        textEdit = QTextEdit()
        textEdit.setText("Window3,The dock widget can be closed,moved,and float")
        dock.setWidget(textEdit)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.setWindowTitle("DockWidget Demo")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())
