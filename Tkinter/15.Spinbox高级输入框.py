'''
    @Spinbox 高级输入框
        Spinbox 是 Entry 控件的升级版，它是 Tkinter 8.4 版本后新增的控件，该控件不仅允许用户直接输入内容，还支持用户使用微调选择器（即上下按钮调节器）来输入内容：

'''

import tkinter as tk

root = tk.Tk()
root.title("C语言中文网")
root.geometry('300x200+300+300')
root.iconbitmap('logo.ico')
# 如果是数字使用 from_和to参数，范围 0-20,并且与2步长递增或递减
w = tk.Spinbox(root, from_=0, to=20, increment=2, width=15, bg='#9BCD9B')
w.pack()
# 显示窗口
root.mainloop()