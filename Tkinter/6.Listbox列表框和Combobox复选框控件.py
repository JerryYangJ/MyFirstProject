'''
    @Listbox 控件
        1.属性：除了共有属性之外，列表框控件也有一些其他属性：
            属性	说明
            listvariable	1. 指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目
                            2. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("c c++ java python")
            selectbackground	1. 指定当某个项目被选中的时候背景颜色，默认值由系统指定
            selectborderwidth	1. 指定当某个项目被选中的时候边框的宽度
                                2. 默认是由 selectbackground 指定的颜色填充，没有边框
                                3. 如果设置了此选项，Listbox 的每一项会相应变大，被选中项为 "raised" 样式
            selectforeground	1. 指定当某个项目被选中的时候文本颜色，默认值由系统指定
            selectmode	1. 决定选择的模式，tk 提供了四种不同的选择模式，分别是："single"（单选）、"browse"（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现），默认是 "browse"
            setgrid	指定一个布尔类型的值，决定是否启用网格控制，默认值是 False
            takefocus	指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来），默认值是 True
            xscrollcommand	为 Listbox 组件添加一条水平滚动条，将此选项与 Scrollbar 组件相关联即可
            yscrollcommand	为 Listbox 组件添加一条垂直滚动条，将此选项与 Scrollbar 组件相关联即可  

        2.方法：  
            方法	说明
            activate(index)	将给定索引号对应的选项激活，即文本下方画一条下划线
            bbox(index)	返回给定索引号对应的选项的边框，返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)， xoffset 和 yoffset 表示距离左上角的偏移位置
            curselection()	返回一个元组，包含被选中的选项序号（从 0 开始）
            delete(first, last=None)	 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项
            get(first, last=None)	返回一个元组，包含参数 first 到 last 范围内（包含 first 和 last）的所有选项的文本
            index(index)	返回与 index 参数相应选项的序号
            itemcget(index, option)	获得 index 参数指定的项目对应的选项（由 option 参数指定）
            itemconfig(index, **options)	设置 index 参数指定的项目对应的选项（由可变参数 **option 指定）
            nearest(y)	返回与给定参数 y 在垂直坐标上最接近的项目的序号
            selection_set(first, last=None)	设置参数 first 到 last 范围内（包含 first 和 last）选项为选中状态，使用 selection_includes(序号) 可以判断选项是否被选中。 
            size()	返回 Listbox 组件中选项的数量
            xview(*args)	该方法用于在水平方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现。 如果第一个参数是 "moveto"，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端；如果第一个参数是 "scroll"，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 "units" 或 "pages"），例如：xview("scroll", 2, "pages")表示向右滚动二行。
            yview(*args)	该方法用于在垂直方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现   
        
        3.Listbox列表框组件:
        -向列表框组件插入文本项：
            Listbox.insert(index,item)
        -返回选中项目的索引：返回结果为元组
            Listbox.curselection()
        -删除文本项：
            Listbox.delete(first,last)  删除从first到last的项目，不指定last时删除1个项目
        -获取项目内容
            Listbox.get(first,last)
        -获取项目个数
            Listbox.size()
        -获取Listobx内容：需要使用listvariable属性为Listbox对象指定一个对于的变量，通过get()方法获取内容
            m=StringVar()
            listb=Listbox(root,listvariable=m)
            listb.pack()
            ront.mainloop()
            print(m.get())
        -多选，单选：
            -将selectmode属性设置为MULTIPLE为多选
            -将selectmode属性设置为SINGLE为单选
            
    @Combobox 控件 
        不过需要注意的是 Combobox 并不包含在 tkinter 模块中，而是包含在tkinter.ttk子模块中，因此若想使用 Combobox 控件，需要使用下面的导包方式：
            from tkinter import ttk
        与Listbox用法相同
            -get()：获取当前选中选项的内容
            -current(): 获取当前选中选项的索引值
'''  # Listbox/Conbobox

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win = Tk()
win.title('Listbox控件示例')
win.geometry('400x400')
win.iconbitmap('logo.ico')
# 添加滚动条
s = Scrollbar(win)
s.pack(side=RIGHT, fill=Y)
# 创建列表选项
listbox1 = Listbox(win, selectmode=MULTIPLE, height=5, yscrollcommand=s.set)
# i表示索引值，item表示值，根据索引值的位置依次插入
for i, item in enumerate(['塑料生产部', '质量控制部', '供应链', '研发部', '1', '2', '3', '4', '5']):
    listbox1.insert(i, item)
listbox1.pack()

# 设置滚动条，使用yview使其在垂直方向上滚动Listbox组件的内容，通过绑定Scollbar组件command参数实现
s.config(command=listbox1.yview)

# 使用匿名函数，创建删除函数，点击删除按钮会删除选项
bt = Button(win, text='删除', command=lambda x=listbox1: x.delete(ACTIVE))
# 将按钮放置在底部
bt.pack(side=BOTTOM)

# 通过StringVar()方法动态获取列表框中的选项
var1 = StringVar()
l = Label(win, bg="#B0B0B0", font=('微软雅黑', 15), width=20, textvariable=var1)
l.pack()


# 创建一个按钮的点击事件
def click_button():
    # 使用curselection来选中文本
    try:
        val = listbox1.get(listbox1.curselection())
        var1.set(val)
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e, '没有选则任何条目')


b1 = Button(win, text='获取当前选项', command=click_button)
b1.pack()

cbox = ttk.Combobox(win)
cbox.pack()
cbox['value'] = ('塑料生产部', '质量控制部', '供应链', '研发部')
# 设置默认选项索引值
cbox.current(3)


# 回调函数，绑定执行事件，向文本中插入选中文本
def func(event):
    text.insert('insert', cbox.get() + '\n')


# 绑定下拉菜单事件
cbox.bind('<<ComboboxSelected>>', func)
text = Text(win)
text.pack()
win.mainloop()
