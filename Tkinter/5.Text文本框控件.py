'''
    @Text 控件
        Text 控件用于显示和编辑多行文本
        1.除了基本的共有属性之外，Text 控件还具备以下属性：            
            属性	说明
            autoseparators	默认为 True，表示执行撤销操作时是否自动插入一个“分隔符”（其作用是用于分隔操作记录）
            exportselection	默认值为 True，表示被选中的文本是否可以被复制到剪切板，若是 False 则表示不允许。
            insertbackground	设置插入光标的颜色，默认为 BLACK
            insertborderwidth	设置插入光标的边框宽度，默认值为 0
            insertofftime	该选项控制光标的闪烁频频率（灭的状态）
            insertontime	该选项控制光标的闪烁频频率（亮的状态）
            selectbackground	指定被选中文本的背景颜色，默认由系统决定
            selectborderwidth	指定被选中文本的背景颜色，默认值是0
            selectforeground	指定被选中文本的字体颜色，默认值由系统指定
            setgrid	默认值是 False，指定一个布尔类型的值，确定是否启用网格控制
            spacing1	指定 Text 控件文本块中每一行与上方的空白间隔，注意忽略自动换行，且默认值为 0。
            spacing2	指定 Text 控件文本块中自动换行的各行间的空白间隔，忽略换行符，默认值为0
            spacing3	指定 Text 组件文本中每一行与下方的空白间隔，忽略自动换行，默认值是 0
            tabs	定制 Tag 所描述的文本块中 Tab 按键的功能，默认被定义为 8 个字符宽度，比如 tabs=('1c', '2c', '8c') 表示前 3 个 Tab 宽度分别为 1厘米，2厘米，8厘米。
            undo	该参数默认为 False，表示关闭 Text 控件的“撤销”功能，若为 True 则表示开启
            wrap	该参数用来设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行，参数值 none（不自动换行）、char（按字符自动换行）、word（按单词自动换行）
            xscrollcommand	该参数与 Scrollbar 相关联，表示沿水平方向上下滑动
            yscrollcommand	该参数与 Scrollbar 相关联，表示沿垂直方向左右滑动
        2.常用方法：
            方法	说明
            bbox(index)	返回指定索引的字符的边界框，返回值是一个 4 元组，格式为(x,y,width,height)
            edit_modified()	该方法用于查询和设置 modified 标志（该标标志用于追踪 Text 组件的内容是否发生变化）
            edit_redo()	“恢复”上一次的“撤销”操作，如果设置 undo 选项为 False，则该方法无效。
            edit_separator()	插入一个“分隔符”到存放操作记录的栈中，用于表示已经完成一次完整的操作，如果设置 undo 选项为 False，则该方法无效。
            get(index1, index2)	返回特定位置的字符，或者一个范围内的文字。
            image_cget(index, option)	返回 index 参数指定的嵌入 image 对象的 option 选项的值，如果给定的位置没有嵌入 image 对象，则抛出 TclError 异常
            image_create()	在 index 参数指定的位置嵌入一个 image 对象，该 image 对象必须是 Tkinter 的 PhotoImage 或 BitmapImage 实例。
            insert(index, text)	在 index 参数指定的位置插入字符串，第一个参数也可以设置为 INSERT，表示在光标处插入，END 表示在末尾处插入。
            delete(startindex [, endindex])	删除特定位置的字符，或者一个范围内的文字。
            see(index)	如果指定索引位置的文字是可见的，则返回 True，否则返回 False。      
                Index 索引
                    索引类型	说明
                    INSERT	对应插入光标的位置
                    CURRENT	对应与鼠标坐标最接近的位置
                    END	对应 Text 控件的文本域中最后一个字符的下一个位置
                    "line.column"	表示某一行某一列的一个位置，比如 1.2 表示第一行第二列的一个位置
                    "line.end"	表示某一行到末尾的最后一个位置
                    SEL	一种针对于 Tag 的特殊索引用法，(SEL_FIRST,SEL_LAST) 表示当前被选中的范围      
'''  # Text控件

from tkinter import *

win = Tk()
win.title('Text控件示例')
win.iconbitmap('logo.ico')
win.geometry('400x420')

# 创建一个文本控件
text = Text(win, width=50, height=30, undo=True, autoseparators=False)
# 适用pack(fill= X )可以设置文本域的填充模式。比如X标识水平方向填充，Y标识沿垂直方向填充，BOTH表示沿水平、垂直方向填充
text.grid()
# INSERT光标处插入；END末尾处插入
text.insert(INSERT, '这是一个Text控件的演示示例')


# 定义撤销和恢复的方法
def backout():
    text.edit_undo()


def regain():
    text.edit_redo()

# 定义撤销和恢复按钮
Button(win, text='撤销', command=backout).grid(row=3, column=0, sticky='w', padx=10, pady=5)
Button(win, text='恢复', command=regain).grid(row=3, column=0, sticky='e', padx=10, pady=5)


win.mainloop()
