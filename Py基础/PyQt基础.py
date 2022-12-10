# @Time :2022/10/21 15:23
# @Author : Jerry Y
# @File  : PyQt基础.py
# @Info  :

'''
三种窗口类型：
    QMainWindow:可以包含菜单栏、工具栏和标题栏，是最常见的窗口形式，可以通过setCentralWidget()设置主部件
    QDialog:是对话窗口的基类，没有菜单栏、工具栏和标题栏
    QWidget：不确定窗口的用途，就是用QWidget.一般用作其他部件的子部件
    我们一般会使用QMainWindow,在QMainWindow里面使用QDialog，偶尔使用QWidget

1、设置窗口风格
    Qt实现的窗口样式默认使用的是当前操作系统的原生窗口样式，在不同操作系统下原生窗口样式显示的风格是不一样的。
    可以为每个Widget设置风格：
    setStyle(QStyle style)
    获取当前平台支持的原有QStyle样式
    QStyleFactory.keys()
    对QApplication设置QStyle样式
    QApplication.setStyle(QStyleFactory.create(“WindowsXP”))
    如果其它Widget没有设置QStyle，则默认使用QApplication使用的QStyle。
2、设置窗口样式
    PyQt5使用setWindowFlags（Qt.WindowFlags）函数设置窗口样式。
    Qt的窗口类型如下：
    Qt.Widget：默认窗口，有最大化、最小化、关闭按钮
    Qt.Window：普通窗口，有最大化、最小化、关闭按钮
    Qt.Dialog：对话框窗口，有问号和关闭按钮
    Qt.Popup：弹出窗口，窗口无边框
    Qt.ToolTip：提示窗口，窗口无边框，无任务栏
    Qt.SplashScreen：闪屏，窗口无边框，无任务栏
    Qt.SubWindow：子窗口，窗口无按钮，但有标题栏
    Qt自定义的顶层窗口外观标识：
    Qt.MSWindowsFixedSizeDialogHint：窗口无法调整大小
    Qt.FrameLessWindowHint：窗口无边框
    Qt.CustomWinodwHint：有边框但无标题栏和按钮，不能移动和拖动
    Qt.WindowTitleHint：添加一个标题栏和一个关闭按钮
    Qt.WindowSystemMenuHint：添加系统目录和一个关闭按钮
    Qt.WindowMaximizeButtonHint：激活最大化和关闭按钮，禁止最小化按钮
    Qt.WindowMinimizeButtonHint：激活最小化和关闭按钮，禁止最大化按钮
    Qt.WindowMinMaxButtonsHint：激活最大化、最小化和关闭按钮
    Qt.WindowCloseButtonHint：增加一个关闭按钮
    Qt.WindowContextHelpButtonHint：增加问号和关闭按钮
    Qt.WindowStaysOnTopHint：窗口始终处于顶层位置
    Qt.WindowStaysOnBottomHint：窗口始终处于底层位置
'''
'''
# 相关函数方法
    setWindowTitle()   # 设置主窗口的标题
    resize()   # 设置窗口的大小
    statusBar()  # 创建状态栏
    showMessage('信息',过期时间/秒)  # 状态栏展示的信息
    setWindowIcon(QIcon(图标))  # 设置窗口图标
    QDesktopWidget().screenGeometry()  # 获取屏幕的坐标系
    geometry()  # 获取窗口坐标系
    move()   # 移动窗口
    QPushButton()  # 创建按钮
    QPushButton().clicked.connect(self.onClick_Button)  # 将按钮与槽(自定义函数)绑定，点击按钮触发事件执行函数
    QHBoxLayout()  # 创建水平布局
    QVBoxLayout()  # 创建垂直布局
    mainLayout = QGridLayout()  # 创建栅格布局
    mainLayout.addWidget(控件名,控件位置行索引,控件位置行索引,控件占几行,控件占几列)
    setBuddy()  # 设置伙伴控件
    QHBoxLayout().addWidget()  # 添加组件到水平布局中
    QWidget()  # 子窗口， 
    QWidget().setLayout(布局)  # 将某种布局放到屏幕上
    setCentralWidget(屏幕)  # 让屏幕及框架放到窗口上
    sender = self.sender()  # 可以获取到button
    sender.text()  # 获取到按钮上的内容
    app = QApplication.instance()  # 得到一个实例
    app.quit()   # 退出应用程序
    setFont(QFont('字体', 大小))  # 设置字体和大小
    setToolTip()  # 设置悬浮提示信息
    setGeometry(左右， 上下， 宽， 高)   #第一个参数  是用户区域参照与屏幕左上角坐标原点的x坐标和y坐标，后面两个参数分别是用户区域的宽和高
   
# QLabel控件的基本用法
    QLabel()  # 创建label
    setAlignment(Qt.AlignCenter):设置文本的对齐方式，文本居中对齐
    setPixmap(QPixmap("./images/4.jpg")) #用于在标签或按钮上显示图像，类型又BMP,GIF,JPG等
    setOpenExternalLinks(True)  #要么触发单击事件，要么链接，只能二者选其一,如果设为True用浏览器打开网页，如果设为False，调用槽函数
    setAutoFillBackground(True)  #背景自动填充
    palette = QPalette()  #填充
    palette.setColor(QPalette.Window,Qt.blue) #设置label背景颜色
    setPalette()  # 调试板
    setIndent(): #设置文本缩进
    text(): #获取文本内容
    setBuddy(): #设置伙伴关系
    setText(): #设置文本内容
    selectText(): #返回所选择的字符
    setWordWrap(): #设置是否允许换行
    linkHovered  #当鼠标滑过QLabel控件时触发
    linkActivated # 当鼠标单击QLabel控件时触发

'''

'''
QSS样式设置
1、QSS语法规则
    QSS（Qt Style Sheets），即Qt样式表，是用来自定义控件外观的一种机制。QSS语法规则与CSS大体相同，QSS样式由两部分组成，选择器用于指定哪些
    控件受到影响，声明用于指定哪些属性应该在控件上进行设置。声明部分是一系列的“属性:值”，使用分号分隔各个不同的属性值对，使用大括号将所有的声明
    包括在内。
    QPushButton{color:red;}
    表示设置QPushButton及其子类所有实例的前景色为红色，QPushButton表示选择器，指定所有的QPushButton类及其子类都会受到影响。
    可以使用多个选择器指定相关的声明，使用逗号将各个选择器分隔，如QPushButton,QLineEdit{color:red;}
    
2、QSS选择器类型
    QSS选择器有如下几种类型：
    1、通配选择器：*，匹配所有的控件
    2、类型选择器，如QPushButton，用于匹配所有的类及其子类的实例。
    3、属性选择器：匹配所有的属性及属性值的实例，如QPushButton[name=”okButton”]将匹配所有的name属性为okButton的按钮实例。
    4、类选择器：.ClassName，如.QPushButton用于匹配所有的QPushButton实例，但不匹配其子类。
    5、ID选择器：#objectName，如#okButton匹配所有的ID为okButton的控件，ID即为obejctName。
    6、后代选择器：如QDialog QPushButton，匹配所有的QDialog容器中包含的QPushButton，不管是直接的还是间接的。
    7、子选择器：如QDialog > QPushButton，匹配所有的QDialog容器中包含的QPushButton，要求QPushButton的直接父容器是QDialog。
    
3、QSS子控件
    QSS子控件是一种选择器，通常应用在复杂控件上，如QComboBox，QComboBox有一个矩形的外边框，右边有一个下拉箭头，点击后会弹出下拉列表。
    ::drop-down子控件选择器可以与选择器组合使用，
    QComboBox#combo::drop-down{imge:url(dropdown.png)}表示为指定ID为combo的QComboBox控件的下拉箭头自定义图标。

4、QSS伪状态
    QSS伪状态选择器是以：开头的一个选择表达式，如:hover，表示当鼠标经过时的状态。伪状态选择器限制了当控件处于某种状态时才可以使用的QSS规则，
    伪状态只能描述一个控件或复合控件的子控件状态，因此只能放在选择器的最后面。
    QComboBox::drop-down:hover{background-color:red;}
    
5、QDarkStyleSheet
    QDarkStyleSheet是一个用于PyQt应用的深黑色样式表。
'''

'''
设置窗口背景
    窗口背景主要包括背景色和背景图片。设置窗口背景主要有三种方法：QSS设置窗口背景；QPalette设置窗口背景；paintEvent函数内部使用QPainter绘制
    窗口背景。

'''
'''
PyInstaller:PyInstaller使用时需切换至xxx.py文件所在目录下。

PyInstaller使用命令如下：
    pyinstaller yourprogram.py
        常用可选项如下：
            -F：打包后只生成单个可执行文件
            -D：默认选项，创建一个目录，包含可执行文件以及大量依赖文件
            -c：默认选项，使用控制台
            -w：不使用控制台
            -p：添加搜索路径，让其找到对应的库
            -i：改变生成程序的icon图标。
'''

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("第一个PyQt")
        # 调整窗口大小
        self.resize(300, 200)
        # # 设置窗口在屏幕上的位置
        # w.move(200,200)
        # 设置窗口图标
        self.setWindowIcon(QIcon('../QMS.png'))

        # 添加按钮控件
        self.btn = QPushButton("注册")
        # 设置按钮的父类窗口（将控件添加到窗口）
        self.btn .setParent(self)
        self.btn .setGeometry(50, 80, 70, 30)

        # 添加label
        self.label = QLabel("账号：", self)     # 创建时指定父窗口
        # 设置label位置、大小：x,y,w,h
        self.label.setGeometry(20, 20, 60, 20)

        # 添加文本框
        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("请输入账号")    # 设置占位符文本（默认文本）
        self.edit.setGeometry(80, 20, 200, 20)


if __name__ == '__main__':
    app = QApplication(sys.argv) # 只要是Qt制作的app,必须有且只有一个QApplication对象； sys.argv当作参数的目的是将运行是的命令参数传递给QApplication对象

    # 创建一个窗口对象
    w = MyWin()

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
