# @Time :2022/11/8 13:58
# @Author : Jerry Y
# @File  : QWidget控件.py
# @Info  :


'''
1、大小与位置：
　　x():相对于父控件的位置，顶层控件（没有父控件）则相对于桌面的x位置
　　y():相对于父控件的y位置,顶层控件（没有父控件）则相对于桌面的y位置
　　pos():x和y的组合 QPoint(x, y)
　　width():控件的宽度，不包含任何窗口框架
　　height():控件的高度，不包含任何窗口框架
　　size():width和height的组合 ,QSize(width, height)
　　geometry():用户区域相对于父控件的位置和尺寸组合 QRect(x, y, width, height)
　　rect():0, 0, width, height的组合 QRect(0, 0, width, height)
　　frameSize():框架大小
　　frameGeometry():框架尺寸
　　move(x, y):操控的是x, y；也就是pos 包括窗口框架
　　resize(width, height):操控的是宽高 不包括窗口框架
　　setGeometry(x_noFrame, y_noFrame, width, height):
　　adjustSize():根据内容自适应大小

最大和最小尺寸：
　　minimumWidth()：最小尺寸的宽度
　　minimumHeight()：最小尺寸的高度
　　minimumSize()：最小尺寸
　　maximumWidth()：最大尺寸的宽度
　　maximumHeight()：最大尺寸的高度
　　maximumSize()：最大尺寸
　　setMaximumWidth()：
　　setMaximumHeight()：
　　setMinimumWidth()：
　　setMinimumHeight()：
　　setMinimumSize()

设置内容边距：
　　setContentsMargins(左, 上, 右, 下)
　　getContentsMargins()：获取内容边距
　　contentsRect()：获取内容区域


鼠标相关：
　　setCursor()：设置鼠标形状
　　unsetCursor():重置鼠标
　　cursor() -> QCursor:获取鼠标
　　hasMouseTracking()：判定是否设置了鼠标跟踪
　　setMouseTracking(bool)：设置鼠标是否跟踪 。所谓的鼠标跟踪，其实就是设置检测鼠标移动事件的条件


事件相关：
　　showEvent(QShowEvent)：控件显示时调用
　　closeEvent(QCloseEvent)：控件关闭时调用
　　moveEvent(QMoveEvent)：控件移动时调用
　　resizeEvent(QResizeEvent)：控件调整大小时调用
　　enterEvent(QEvent)：鼠标进入时触发
　　leaveEvent(QEvent)：鼠标离开时触发
　　mousePressEvent(QMouseEvent)：
　　mouseReleaseEvent(QMouseEvent)：
　　mouseDoubleClickEvent(QMouseEvent)
　　mouseMoveEvent(QMouseEvent)：鼠标按下后移动时触发
　　keyPressEvent(QKeyEvent)：键盘按下时调用
　　keyReleaseEvent(QKeyEvent)：
　　focusInEvent(QFocusEvent)：获取焦点时调用
　　focusOutEvent(QFocusEvent)：失去焦点时调用
　　dragEnterEvent(QDragEnterEvent)：拖拽进入控件时调用
　　dragLeaveEvent(QDragLeaveEvent)：拖拽离开控件时调用
　　dragMoveEvent(QDragMoveEvent)：拖拽在控件内移动时调用
　　dropEvent(QDropEvent)：拖拽放下时调用
　　paintEvent(QPaintEvent)：显示控件, 更新控件时调用
　　changeEvent(QEvent)：窗体改变, 字体改变时调用
　　contextMenuEvent(QContextMenuEvent)：访问右键菜单时调用
　　inputMethodEvent(QInputMethodEvent)：输入法调用


父子关系：
　　childAt(x, y)：获取在指定坐标的控件。（根据当前点击的坐标获取子控件）
　　parentWidget()：获取指定控件的父控件
　　childrenRect()：所有子控件组成的边界矩形


'''