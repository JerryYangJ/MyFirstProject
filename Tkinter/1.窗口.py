'''
    窗口常用方法：
        函数	说明
        window.title("my title")	接受一个字符串参数，为窗口起一个标题
        window.resizable()	是否允许用户拉伸主窗口大小，默认为可更改，当设置为 resizable(0,0)或者resizable(False,False)时不可更改
        window.geometry()	设定主窗口的大小以及位置，当参数值为 None 时表示获取窗口的大小和位置信息。
        window.quit()	关闭当前窗口
        window.update()	刷新当前窗口
        window.mainloop()	设置窗口主循环，使窗口循环显示（一直显示，直到窗口被关闭）
        window.iconbitmap()	设置窗口左上角的图标（图标是.ico文件类型）
        window.config(background ="red")	设置窗口的背景色为红色，也可以接受 16 进制的颜色值
        window.minsize(50,50)	设置窗口被允许调整的最小范围，即宽和高各50
        window.maxsize(400,400)	设置窗口被允许调整的最大范围，即宽和高各400
        window.attributes("-alpha",0.5)	用来设置窗口的一些属性，比如透明度（-alpha）、是否置顶（-topmost）即将主屏置于其他图标之上、是否全屏（-fullscreen）全屏显示等
        window.state("normal")	用来设置窗口的显示状态，参数值 normal（正常显示），icon（最小化），zoomed（最大化），
        window.withdraw()	用来隐藏主窗口，但不会销毁窗口。
        window.iconify()	设置窗口最小化
        window.deiconify()	将窗口从隐藏状态还原
        window.winfo_screenwidth()
        window.winfo_screenheight()	获取电脑屏幕的分辨率（尺寸）
        window.winfo_width()
        window.winfo_height() 	获取窗口的大小，同样也适用于其他控件，但是使用前需要使用 window.update() 刷新屏幕，否则返回值为1
        window.protocol("协议名",回调函数)	启用协议处理机制，常用协议有 WN_DELETE_WINDOW，当用户点击关闭窗口时，窗口不会关闭，而是触发回调函数。
'''  # 窗口

import tkinter as tk

win = tk.Tk()
# 设置窗口titile
win.title('窗口练习')
# 设置窗口的大小：宽x高,及显示的位置+200+300
win.geometry('450x300+200+300')
# 获取电脑屏幕的大小
print(f'电脑屏幕的分辨率是{win.winfo_screenwidth()}x{win.winfo_screenheight()}')
# 要求窗口的大小，必须先刷新一次
win.update()
print(f'窗口的分辨率是{win.winfo_width()}x{win.winfo_height()}')
# 设置窗口不能被拉伸
# win.resizable(0, 0)
# 改变背景颜色
win.config(background='#6fb765')
# 设置窗口处于顶层
win.attributes('-topmost', True)
# 设置窗口的透明度
win.attributes('-alpha', 1)
# 设置窗口被允许最大调整的范围，与resizable冲突
win.maxsize(600, 600)
# 设置窗口被允许最小调整的范围，与resizable冲突
win.minsize(50, 50)
# 更改左上角窗口的icon图标，加载图表logo
# win.iconbitmap(path)

# 添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
text = tk.Label(win, text='窗口测试', bg='yellow', fg='red', font=('Times', 15, 'bold italic underline'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，通过command参数设置关闭窗口的功能
button = tk.Button(win, text="关闭", command=win.quit)
# 将按钮放置在主窗口内
button.pack(side='bottom')
# 进入主循环，显示主窗口
win.mainloop()
