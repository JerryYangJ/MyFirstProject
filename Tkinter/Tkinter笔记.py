'''
    @ GUI工具包
        wxPython：   是Python的一套优秀的GUI图形库
        Kivy：       是一个开源工具包，能让使用相同源代码的程序能跨平台运行
        Flexx：      纯Python工具包，用来创建图形化应用程序，可使用Web技术进行界面的渲染
        PyQt：       是Qt库的Python版本，支持跨平台
        Tkinter：    是Tk图形用户界面工具包标准的Python接口，轻量级跨平台用户界面开发工具
        Pywin32：    允许像VC一样的形式使用Python开发win32应用
        PyGTK：      用Python轻松创建具有图形用户界面的程序
        pyui4win：   开源的采用自绘技术的界面库

'''

'''
    @ Tkinter组件说明
    1.组件类型：
        控件类型	控件名称	控件作用
        Button	按钮	点击按钮时触发/执行一些事件（函数）
        Canvas	画布	提供绘制图，比如直线、矩形、多边形等
        Checkbutton	复选框	多项选择按钮，用于在程序中提供多项选择框
        Entry	文本框输入框	用于接收单行文本输入
        Frame	框架（容器）控件	定义一个窗体（根窗口也是一个窗体），用于承载其他控件，即作为其他控件的容器
        Lable	标签控件	用于显示单行文本或者图片
        LableFrame	容器控件	一个简单的容器控件，常用于复杂的窗口布局。
        Listbox	列表框控件	以列表的形式显示文本
        Menu	菜单控件	菜单组件（下拉菜单和弹出菜单）
        Menubutton	菜单按钮控件	用于显示菜单项
        Message	信息控件	用于显示多行不可编辑的文本，与 Label控件类似，增加了自动分行的功能
        messageBox	消息框控件	定义与用户交互的消息对话框
        OptionMenu	选项菜单	下拉菜单
        PanedWindow	窗口布局管理组件	为组件提供一个框架，允许用户自己划分窗口空间
        Radiobutton	单选框	单项选择按钮，只允许从多个选项中选择一项
        Scale	进度条控件	定义一个线性“滑块”用来控制范围，可以设定起始值和结束值，并显示当前位置的精确值
        Spinbox	高级输入框	Entry 控件的升级版，可以通过该组件的上、下箭头选择不同的值
        Scrollbar	滚动条	默认垂直方向，鼠标拖动改变数值，可以和 Text、Listbox、Canvas等控件配合使用
        Text	多行文本框	接收或输出多行文本内容
        Toplevel	子窗口	在创建一个独立于主窗口之外的子窗口，位于主窗口的上一层，可作为其他控件的容器
        tkMessageBox：显示应用程序的消息框
            
    2.组件属性：
        属性名称	说明
        anchor	定义控件或者文字信息在窗口内的位置。锚点（内容停靠位置）
        bg	bg 是 background 的缩写，用来定义控件的背景颜色，参数值可以颜色的十六进制数，或者颜色英文单词
        bitmap	定义显示在控件内的位图文件
        borderwidth	定于控件的边框宽度，单位是像素
        command	该参数用于执行事件函数，比如单击按钮时执行特定的动作，可将执行用户自定义的函数
        cursor	当鼠标指针移动到控件上时，定义鼠标指针的类型，字符串格式，参数值有 crosshair（十字光标）watch（待加载圆圈）plus（加号）arrow（箭头）等
        font	若控件支持设置标题文字，就可以使用此属性来定义，它是一个数组格式的参数 (字体,大小，字体样式)
        fg	fg 是 foreground 的缩写，用来定义控件的前景色，也就是字体的颜色
        height	该参数值用来设置控件的高度，文本控件以字符的数目为高度（px），其他控件则以像素为单位
        image	定义显示在控件内的图片文件
        justify	定义多行文字的排列方式，此属性可以是 LEFT/CENTER/RIGHT
        padx/pady	定义控件内的文字或者图片与控件边框之间的水平/垂直距离
        relief	定义控件的边框样式，参数值为FLAT（平的）/RAISED（凸起的）/SUNKEN（凹陷的）/GROOVE（沟槽桩边缘）/RIDGE（脊状边缘）
        text	定义控件的标题文字
        state	控制控件是否处于可用状态，参数值默认为 NORMAL/DISABLED，默认为 NORMAL（正常的）
        width	用于设置控件的宽度，使用方法与 height 相同
        dimension:大小
        color：颜色
        state：组件状态。normal\active\disabled
        
        -组件属性设置的三种方法
            -button=Button(root,text="确定“）  # 构造函数
            -button.config(text=”确定“)   # 组件对象的config()方法的命名参数
            -button['text']="确定”        # 组件对象的属性赋值
            
    3.组件绑定的函数传递参数，事件传递参数，使用lambda函数
        -btn = Tkinter.Button(text='按钮’, command = lambda: click(a=1, b=2 ,c=3))
        -btn.bind('<Button-1>', lambda event:click(1, 2, 3))
    
'''  # Tkinter组件说明


from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def bt1_click():
    text1 = entry_v1.get()
    messagebox.showinfo(title='messagebox', message=f'按钮被按下,获取输入框1的数据为：{text1}')


def bt2_click():
    text2 = entry_v2.get()
    messagebox.showinfo(title='messagebox', message=f'按钮被按下,获取输入框2的数据为：{text2}')


def bt3_click():
    txt = entry_v2.get()
    text.insert(END, txt)


def bt4_click():
    # 使用curselection来选中文本
    try:
        val = listbox.get(listbox.curselection())
        messagebox.showinfo(title='messagebox', message=f'按钮被按下,获取输入框2的数据为：{val}')
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e, '没有选则任何条目')

def bt5_click():
    select_txt = combobox.get()
    select_index = combobox.current()+1
    messagebox.showinfo(title='messagebox', message=f'combobox单选框选择的序号是：{select_index}，内容是：{select_txt}')

def select():
    # strings = '您选择了' + str(v.get())
    strings = site[v.get() - 1][0]
    messagebox.showinfo(title='Radiobutton提醒', message=f'Radiobutton单选框中被选中的是：{strings}')

def command():
    messagebox.showinfo(title='消息', message='你正在使用menu')

# 创建根窗口
root = Tk()
# 设置窗口titile
root.title('tkinter控件大全')
# 设置窗口的大小：宽x高,及显示的位置+200+300
root.geometry('800x600+400+10')
# 更改左上角窗口的icon图标，加载图表logo
root.iconbitmap('logo.ico')
# 获取电脑屏幕的大小
print(f'电脑屏幕的分辨率是{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
# 要求窗口的大小，必须先刷新一次
root.update()
print(f'窗口的分辨率是{root.winfo_width()}x{root.winfo_height()}')
# 设置窗口不能被拉伸
# win.resizable(0, 0)
# 改变背景颜色
root.config(background='#6fb765')
# 设置窗口处于顶层
root.attributes('-topmost', True)
# 设置窗口的透明度
root.attributes('-alpha', 1)
# 设置窗口被允许最大调整的范围，与resizable冲突
root.maxsize(600, 600)
# 设置窗口被允许最小调整的范围，与resizable冲突
root.minsize(50, 50)

# 添加Button控件
bt_frame = LabelFrame(root, text='按钮', bg='red', bd=3)
bt1 = Button(bt_frame, text='entry_按钮1', activebackground='red', activeforeground='blue', fg='blue', font=('微软雅黑', 9),
             command=bt1_click).grid(row=0)
bt2 = Button(bt_frame, text='entry_按钮2', bd=10, command=bt2_click).grid(row=0, column=1)  # 先布局上层才能对下层布局，否则会不显示或布局方式冲突报错
bt3 = Button(bt_frame, text='text_按钮', bd=5, command=bt3_click).grid(row=0, column=2)  # 先布局上层才能对下层布局，否则会不显示或布局方式冲突报错
bt4 = Button(bt_frame, text='listbox_按钮', bd=3, command=bt4_click).grid(row=0, column=3)  # 先布局上层才能对下层布局，否则会不显示或布局方式冲突报错
bt5 = Button(bt_frame, text='combobox_按钮', bd=3, command=bt5_click).grid(row=0, column=4)

# 添加Entry控件
entry_frame = LabelFrame(root, text='输入框')
entry_v1 = StringVar()
entry_v1.set('我是第一个输入框')
entry_v2 = StringVar()
entry_v2.set('我是第二个输入框')
listbox_v = StringVar()
# text_v2 = StringVar()

entry1 = Entry(entry_frame, textvariable=entry_v1).grid(row=0)
entry2 = Entry(entry_frame, textvariable=entry_v2)
# entry2.insert(1, '我是第二个输入框111')
entry2.grid(row=0, column=1)

# 添加text控件
text_frame = LabelFrame(root, text='文本框')
text = Text(text_frame, width=50, height=2, spacing2=3)  # 宽50字符，高2字符
text.insert(END, '我是文本框text')  # 要在布局前插入显示数据，否则报错
text.grid(row=0)

# 添加Listbox控件,并配置scrollbar滚动条
listbox_frame = LabelFrame(root, text='列表框')
xscrollbar = Scrollbar(listbox_frame, orient="horizontal")
yscrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
listbox = Listbox(listbox_frame, width=50, height=5, listvariable=listbox_v, xscrollcommand=xscrollbar.set,
                  yscrollcommand=yscrollbar.set)  # 宽50字符，高2字符
for i, item in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    listbox.insert(i, item)
listbox.grid(row=1)
xscrollbar.grid(row=0, column=1)
yscrollbar.grid(row=1, column=1)
xscrollbar.config(command=listbox.xview)
yscrollbar.config(command=listbox.yview)

# 添加Combobox控件
combobox_frame = LabelFrame(root, text='复选框')
combobox = ttk.Combobox(combobox_frame)
combobox.grid(row=0)
combobox['value'] = ['一', '二', '三', '四', '五']
combobox.current(0) # 设置默认选项索引

# 添加Radiobutton和Checkbutton控件
v = IntVar()
v.set(0)
rc_frame = LabelFrame(root, text='单选框')
site = [('Radiobutton控件示例1', 1),
        ('Radiobutton控件示例2', 2),
        ('Radiobutton控件示例3', 3),
        ('Radiobutton控件示例4', 4)]
for sel, num in site:
    radio_button = Radiobutton(rc_frame, text=sel, variable=v, value=num, command=select)
    radio_button.pack(anchor='w')


rc_frame1 = LabelFrame(root, text='多选框')
check1 = Checkbutton(rc_frame1, text='checkbutton示例1', font=('微软雅黑', '10', 'bold'), fg='#43CD80')
check2 = Checkbutton(rc_frame1, text='checkbutton示例2', font=('微软雅黑', '10', 'bold'), fg='#43CD80')
check3 = Checkbutton(rc_frame1, text='checkbutton示例3', font=('微软雅黑', '10', 'bold'), fg='#43CD80')

check1.select()  # 将第一个复选框annual的variable值设置为onvalue=1，便是选中状态
check1.toggle()  # 取消第一个复选框的选中状态

check1.pack(anchor='n')
check2.pack(anchor='n')
check3.pack(anchor='n')
# 添加Scale控件

# 添加Canvas控件

# 添加Menu控件
main_menu = Menu(root)
filemenu = Menu(main_menu, tearoff=False)
filemenu.add_command(label='新建', command=command, accelerator='Ctrl+N')
filemenu.add_command(label='打开', command=command, accelerator='Ctrl+0')
filemenu.add_command(label='保存', command=command, accelerator='Ctrl+S')
filemenu.add_separator()    # 添加一条分割线
filemenu.add_command(label='退出', command=root.quit)
main_menu.add_cascade(label='文件', menu=filemenu)    # 加一个父菜单，将一个指定的子菜单，通过 menu 参数与父菜单连接，从而创建一个下拉菜单。
main_menu.add_command(label='编辑', command=command)  # 添加一个普通的命令菜单项
main_menu.add_checkbutton(label='格式', command=command)     # 添加一个多选按钮的菜单项
main_menu.add_radiobutton(label='帮助', command=command)  # 添加一个单选按钮的菜单项

menubtn = Menubutton(rc_frame1, text='这是一个按钮菜单，点击我有惊喜哦！', relief='sunk')
menubtn.pack()
btnmenu = Menu(menubtn, tearoff=False)
btnmenu.add_command(label='新建')
btnmenu.add_command(label='删除')
btnmenu.add_command(label='复制')
btnmenu.add_command(label='保存')
menubtn.config(menu=btnmenu)

# 添加Scrollbar控件

bt_frame.pack()
entry_frame.pack()
text_frame.pack()
listbox_frame.pack()
combobox_frame.pack()
rc_frame.pack(side=LEFT)
rc_frame1.pack(side=RIGHT)
root.config(menu=main_menu)



root.mainloop()
