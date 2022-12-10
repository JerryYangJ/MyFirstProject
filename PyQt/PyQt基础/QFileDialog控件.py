# @Time :2022/10/28 11:04
# @Author : Jerry Y
# @File  : QFileDialog控件.py
# @Info  : 文件对话框


'''
基本方法(函数)及其用法
    QFileDialog.getExistingDirectory()   # 返回选中的文件夹路径
    QFileDialog.getOpenFileName()   # 返回选中的文件路径
    QFileDialog.getOpenFileNames()   # 返回选中的多个文件路径
    QFileDialog.getSaveFileName()   # 存储文件

获取文件夹路径的实例：
    QFileDialog.getExistingDirectory(None, "请选择文件夹路径", "D:\\Qt_ui")
    QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "D:\\Qt_ui")
        -第一个参数：有self用self，没有的用None
        -第二个参数：设置窗口名
        -第三个参数：设置默认打开路径
获取多个文件路径实例（选择文件夹）：
    QFileDialog.getOpenFileNames(None, "请选择要添加的文件", path, "Text Files(*.xls);;All Files(*)")
        -第四个参数：列出可以进行筛选的参数，第一个是默认的，多个用双分号分开


'''

# 导入Qt类用于设置对齐方式调用PyQt内置的颜色等
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QPushButton, QWidget, QLineEdit, QHBoxLayout, \
    QFileDialog, QInputDialog


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
        self.resize(800, 600)
        # 设置窗口左上角在屏幕坐标系中的位置
        # 坐标系以左上角的点为原点
        # 调用格式为move(x, y)，单位(px)
        self.move(300, 300)



def btn_clicked():
    """鼠标单击按钮，打开文件选择对话框"""
    # 创建一个对话框对象
    file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/") # 返回文件路径和文件类型，分别接收，默认为All Files
    # file, type = QFileDialog.getOpenFileName(None, "请选择文件", "D:/", "Text File (*.txt)")   # Text File (*.txt, *.xls)为文件过滤器,多筛选条件用;;隔开
    print(file, type)
    text.setText(file)
    if file:
        try:
            with open(file, 'r', encoding='utf-8')as f:
                data = f.read()
        except UnicodeDecodeError:
            data = "不是合法的txt文件"
        except FileNotFoundError:
            data = ""
        label.setText(data)


# 多文件时用于防止非主文件代码执行
if __name__ == '__main__':
    # 实例化基类QApplication
    # sys.argv表示接受用户输入
    # 这里实质上是用户对GUI窗口的键鼠操作
    app = QApplication(sys.argv)
    # 实例化上述定义的窗口类
    main = PyQt5GUIDemo()

    # 布局（嵌套布局）
    layout1 = QHBoxLayout()
    layout = QVBoxLayout()

    layout.addLayout(layout1)   # 将layout1水平布局嵌套在layout垂直布局中

    # 创建button并布局
    btn = QPushButton("打开文件", main)
    layout1.addWidget(btn)
    # 绑定button的槽
    btn.clicked.connect(btn_clicked)

    text = QLineEdit(main)
    layout1.addWidget(text)

    label = QLabel("显示内容", main)
    layout.addWidget(label)

    # 添加一个弹簧
    layout.addStretch()

    # 将布局添加到窗口
    main.setLayout(layout)

    main.show()  # 显示窗口
    # 使窗口正常退出，并释放内存
    sys.exit(app.exec_())
