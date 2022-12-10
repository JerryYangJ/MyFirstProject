'''
    @Entry控件
        Entry 控件是 Tkinter GUI 编程中的基础控件之一，它的作用就是允许用户输入内容，从而实现 GUI 程序与用户的交互，比如当用户登录软件时，输入用户名和密码，此时就需要使用 Entry 控件
        1.Entry 控件除了具备一些共有属性之外，还有一些自身的特殊属性：
            特殊属性名称	说明
            exportselection 	默认情况下，如果在输入框中选中文本会复制到粘贴板，如果要忽略这个功能，可以设置为 exportselection=0
            selectbackground	选中文字时的背景颜色
            selectforeground	选中文字时的前景色
            show	            指定文本框内容以何种样式的字符显示，比如密码可以将值设为 show="*"
            textvariable	    输入框内值，也称动态字符串，使用 StringVar() 对象来设置，而 text 为静态字符串对象
            xscrollcommand	    设置输入框内容滚动条，当输入的内容大于输入框的宽度时使用户

        2.获取Entry、Text组件的内容
            -get():
            -StringVar()对象：蒋Entry的textvariable属性设置为StringVar()变量，通过StringVar()变量的get()和set()函数读取和输出相应文本内容
                s= StringVar()                            #创建StringVar()对象
                s.set("hello")
                entryCd = Entry(root, textvariable=s)     #Entry组件显示s                      
                print(s.get())                            #输出s

        3.Entry 控件还提供了一些常用的方法：
            方法	说明
            delete()	根据索引值删除输入框内的值
            get()	获取输入框内的是
            set()	设置输入框内的值
            insert()	在指定的位置插入字符串
            index()	返回指定的索引值
            select_clear()	取消选中状态
            select_adujst()	确保输入框中选中的范围包含 index 参数所指定的字符，选中指定索引和光标所在位置之前的字符
            select_from (index)	设置一个新的选中范围，通过索引值 index 来设置
            select_present()	返回输入框是否有处于选中状态的文本，如果有则返回 true，否则返回 false。
            select_to()	选中指定索引与光标之间的所有值
            select_range()	选中指定索引与光标之间的所有值，参数值为 start,end，要求 start 必须小于 end。       

        4.注意：在 Entry 控件中，我们可以通过以下方式来指定字符的所在位置：
            -数字索引：表示从 0 开始的索引数字；
            -"ANCHOE"：在存在字符的情况下，它对应第一个被选中的字符；
            -"END"：对应已存在文本中的最后一个位置；
            -"insert(index,'字符')：将字符插入到 index 指定的索引位置。

        5.Entry 控件的验证功能:
            参数	说明
            validate	指定验证方式，字符串参数，参数值有 focus、focusin、focusout、key、all、none。 
                参数值	说明
                focus	当 Entry 组件获得或失去焦点的时候验证
                focusin	当 Entry 组件获得焦点的时候验证
                focuson	当 Entry 组件失去焦点的时候验证
                key	当输入框被编辑的时候验证
                all	当出现上边任何一种情况的时候验证
                none	 默认不启用验证功能，需要注意的是这里是字符串的 'none'
            validatecommand	指定用户自定义的验证函数，该函数只能返回 True 或者 Fasle
            invalidcommand	当 validatecommand 指定的验证函数返回 False 时，可以使用该参数值再指定一个验证函数。
'''  # Entry控件

import tkinter as tk
import time

win = tk.Tk()
win.iconbitmap('logo.ico')
win.geometry('450x150+100+100')
win.resizable(0, 0)
win.title('电子时钟-Clock')

# 获取当前时间的函数
def gettime():
    # 获取当前时间
    dstr.set(time.strftime('%H:%M:%S'))
    # 每隔1s调用一次gettime()函数来获取时间
    win.after(1000, gettime)

# 生成动态字符串
dstr = tk.StringVar()
# 利用textvariable来实现文本变化
lb = tk.Label(win, textvariable=dstr, fg='green', font=('微软雅黑', 85))
lb.pack()
gettime()
win.mainloop()