'''
    @Tkinter 还提供了三种对话框控件：
        文件选择对话框：filedailog
        颜色选择对话框：colorchooser
        消息对话框：messagebox

        filedailog
            文件对话框被封装在tkinter.filedailog模块中，该模块提供了有关文件对话框的常用函数"
                方法	说明
                Open()	打开个某个文件
                SaveAs()	打开一个保存文件的对话框
                askopenfilename()	打开某个文件，并以包函文件名的路径作为返回值
                askopenfilenames()	同时打开多个文件，并以元组形式返回多个文件名
                askopenfile()	打开文件，并返回文件流对象
                askopenfiles()	打开多个文件，并以列表形式返回多个文件流对象
                asksaveasfilename()	选择以什么文件名保存文件，并返回文件名
                asksaveasfile()	选择以什么类型保存文件，并返回文件流对象
                askdirectory	选择目录，并返回目录名

                参数	说明
                defaultextension	指定文件的后缀名，当保存文件时自动添加文件名，如果自动添加了文件的后缀名，则该选项值不会生效
                filetypes	指定筛选文件类型的下拉菜单选项，该选项值是由 2 元祖构成的列表，其中每个二元祖由两部分组成 (类型名,后缀)，比如 filetypes = [("PNG","*.png"), ("JPG", "*.jpg"), ("GIF","*.gif"),("文本文件","*.txt")...]
                initialdir	指定打开/保存文件的默认路径，默认路径是当前文件夹
                parent	 如果不指定该选项，那么对话框默认显示在根窗口上，通过设置该参数可以使得对话框显示在子窗口上
                title	指定文件对话框的标题

        colorchooser
            颜色选择对话框（colorchooser），提供了一个非常友善的颜色面板，它允许用户选择自己所需要的颜色。 当用户在面板上选择一个颜色并按下“确定”按钮后，它会返回一个二元组，其第 1 个元素是选择的 RGB 颜色值，第 2 个元素是对应的 16 进制颜色值。
            方法	说明
            askcolor()	打开一个颜色对话框，并将用户选择的颜色值以元组的形式返回（没选择返回None），格式为((R, G, B), "#rrggbb")
            Chooser()	打开一个颜色对话框，并用户选择颜色确定后，返回一个二元组，格式为（(R, G, B), "#rrggbb"）
            属性	说明
            default	要显示的初始的颜色，默认颜色是浅灰色（light gray）
            title	指定颜色选择器标题栏的文本，默认标题为“颜色”
            parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
            2. 如果想要将对话框显示在子窗口上，那么可以设置 parent = 子窗口对象

        messagebox
            消息对话框主要起到信息提示、警告、说明、询问等作用，通常配合“事件函数”一起使用，比如执行某个操作出现了错误，然后弹出错误消息提示框
            方法	说明
            askokcancel(title=None, message=None)	打开一个“确定／取消”的对话框
            askquestion(title=None, message=None)	打开一个“是／否”的对话框。
            askretrycancel(title=None, message=None)	打开一个“重试／取消”的对话框
            askyesno(title=None, message=None)	打开一个“是／否”的对话框
            showerror(title=None, message=None)	打开一个错误提示对话框
            showinfo(title=None, message=None)	打开一个信息提示对话框
            showwarning(title=None, message=None)	打开一个警告提示对话框
            属性	说明
            default	1. 设置默认的按钮（也就是按下回车响应的那个按钮）
                    2. 默认是第一个按钮（像“确定”，“是”或“重试”）
                    3. 可以设置的值根据对话框函数的不同，可以选择 CANCEL，IGNORE，OK，NO，RETRY 或 YES
            icon	1. 指定对话框显示的图标
                    2. 可以指定的值有：ERROR，INFO，QUESTION 或 WARNING
                    3. 注意：不能指定自己的图标
            parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
                    2. 如果想要将对话框显示在子窗口上，那么可以设置 parent= 子窗口对象
'''