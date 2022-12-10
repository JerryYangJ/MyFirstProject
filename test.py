import sys

# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    print('开始。。。。')
    
    app = QApplication(sys.argv) # 只要是Qt制作的app,必须有且只有一个QApplication对象； sys.argv当作参数的目的是将运行是的命令参数传递给QApplication对象

    # 创建一个窗口对象
    w =QWidget()

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
