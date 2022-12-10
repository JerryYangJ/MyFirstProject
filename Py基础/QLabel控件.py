# @Time :2022/10/27 17:04
# @Author : Jerry Y
# @File  : QLabel控件.py
# @Info  : 标签


'''
基本方法(函数)及其用法
    setAlignment()：设置文本对齐方式
    setIndent()：设置文本缩进
    text()：获取文本内容
    setBuddy()：设置伙伴关系（伙伴控件）
    setText()：设置文本内容，支持HTML标签(超链接)
    selectedText()：返回所选字符
    setWordWrap()：设置是否允许换行
    setToolTip()：设置按钮提示

常用的信号（事件）
    当鼠标滑过QLabel控件时触发：linkHovered
    当鼠标单击QLabel控件时触发：linkActivated


'''

# 导入Qt类用于设置对齐方式调用PyQt内置的颜色等
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget


# 定义窗口类，继承自父类QMainWindow
class PyQt5GUIDemo(QWidget):
    def __init__(self):
        # 继承父类的属性
        # 也可简写为super().__init__()
        super(PyQt5GUIDemo, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle("我的GUIDemo")
        # 设置窗口的宽、高，单位为屏幕像素(px)
        self.resize(400, 300)
        # 设置窗口左上角在屏幕坐标系中的位置
        # 坐标系以左上角的点为原点
        # 调用格式为move(x, y)，单位(px)
        self.move(300, 300)


def Hovered(self):
    print('鼠标滑过label2触发事件')


def Clicked(self):
    print('鼠标单击label4触发事件')


# 多文件时用于防止非主文件代码执行
if __name__ == '__main__':
    # 实例化基类QApplication
    # sys.argv表示接受用户输入
    # 这里实质上是用户对GUI窗口的键鼠操作
    app = QApplication(sys.argv)
    # 实例化上述定义的窗口类
    main = PyQt5GUIDemo()

    # 垂直布局
    layout = QVBoxLayout()

    # # 添加一个弹簧
    # layout.addStretch(1)

    # 创建label并布局
    label1 = QLabel("标签1", main)
    layout.addWidget(label1)

    # 添加一个弹簧
    layout.addStretch(1)

    label2 = QLabel("标签2", main)
    layout.addWidget(label2)

    # 添加一个弹簧
    layout.addStretch(1)

    label3 = QLabel("标签3", main)
    layout.addWidget(label3)

    # 添加一个弹簧
    layout.addStretch(1)
    label4 = QLabel("标签4", main)
    layout.addWidget(label4)

    # 添加一个弹簧
    layout.addStretch(2)

    label1.setText("<font color=yellow>文本标签</font>")
    # 设置显示背景色
    label1.setAutoFillBackground(True)
    palette = QPalette()
    palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
    label1.setPalette(palette)
    # 居中对齐
    label1.setAlignment(Qt.AlignCenter)

    label2.setText("<a href='#'>GUI实例</a>")

    # 设置居中对齐
    label3.setAlignment(Qt.AlignCenter)
    # 设置提示信息
    label3.setToolTip('图片标签')
    # 设置像素图片
    label3.setPixmap(QPixmap("../image.jpg"))

    # 如果设为True，用浏览器打开网页
    # 如果设为False，调用槽函数
    label4.setOpenExternalLinks(True)

    label4.setText("<a href='https://www.baidu.com'>百度一下</a>")
    # 设置右对齐
    label4.setAlignment(Qt.AlignRight)
    label4.setToolTip('超链接')

    label2.linkHovered.connect(Hovered)

    label4.linkActivated.connect(Clicked)

    # 将布局添加到窗口
    main.setLayout(layout)

    main.show()  # 显示窗口
    # 使窗口正常退出，并释放内存
    sys.exit(app.exec_())
