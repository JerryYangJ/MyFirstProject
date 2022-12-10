'''
    @Button控件
        常用属性：
        属性	说明
        anchor	控制文本所在的位置，默认为中心位置（CENTER）
        activebackground	当鼠标放在按钮上时候，按妞的背景颜色
        activeforeground	当鼠标放在按钮上时候，按钮的前景色
        bd	按钮边框的大小，默认为 2 个像素
        bg	按钮的背景色
        command	用来执行按钮关联的回调函数。当按钮被点击时，执行该函数
        fg	按钮的前景色
        font	按钮文本的字体样样式
        height	按钮的高度
        highlightcolor	按钮控件高亮处要显示的颜色
        image	按钮上要显示的图片
        justify	按钮显示多行文本时，用来指定文本的对齐方式，参数值有 LEFT/RIGHT/CENTER
        padx/pady	padx 指定 x 轴（水平方向）的间距大小，pady 则表示 y轴（垂直方向）的间距大小
        ipadx/ipady	ipadx 指标签文字与标签容器之间的横向距离；ipady 则表示标签文字与标签容器之间的纵向距离
        state	设置按钮的可用状态，可选参数有NORMAL/ACTIVE/DISABLED，默认为 NORMAL
        text	按钮控件要显示的文本

'''  # Button控件

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('Button控件示例')
win.geometry('400x300+300+200')



# 设置回调函数
def bt_callback():
    # 使用消息对话框控件，showinfo()方法显示
    messagebox.showinfo(title='提示', message='按钮被点击，回调函数生效')

# 创建图片对象
im = tk.PhotoImage(file='QMS.png')

# 通过image参数传递图片对象

# 使用按钮控件调用函数
b = tk.Button(win, image=im, text='点击执行回调函数', command=bt_callback)
b.pack()
win.mainloop()
