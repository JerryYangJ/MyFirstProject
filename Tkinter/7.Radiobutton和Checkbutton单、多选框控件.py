'''
    @Radiobutton 单选框控件
        1.特有属性：
            属性	说明
            activebackground	设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的背景色，默认值由系统指定
            activeforeground	设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的前景色，默认值由系统指定
            compound	1. 默认值为 None，控制 Radiobutton 中文本和图像的混合模式，默认情况下，如果有指定位图或图片，则不显示文本
                        2. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
                        3. 设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边，比如如"bottom"，则显示图像在文本的下方。
            disabledforeground	指定当 Radiobutton 不可用的时的前景色颜色，默认由系统指定
            indicatoron	1. 该参数表示选项前面的小圆圈是否被绘制，默认为 True，即绘制；
                        2. 如果设置为 False，则会改变单选按钮的样式，当点击时按钮会变成 "sunken"（凹陷），再次点击变为 "raised"（凸起）
            selectcolor	设置当 Radiobutton 为选中状态的时候显示的图片；如果没有指定 image 选项，该选项被忽略
            takefocus	如果是 True，该组件接受输入焦点，默认为 False
            variable	表示与 Radiobutton 控件关联的变量，注意同一组中的所有按钮的 variable 选项应该都指向同一个变量，通过将该变量与 value 选项值对比，可以判断用户选中了哪个按钮。
            value       单选按钮选中时变量的值
        2.方法：
            方法	说明
            deselect()	取消该按钮的选中状态
            flash()	刷新 Radiobutton 控件，该方法将重绘 Radiobutton控件若干次（即在"active" 和 "normal" 状态间切换）
            invoke()	1. 调用 Radiobutton 中 command 参数指定的函数，并返回函数的返回值
                        2. 如果 Radiobutton 控件的 state(状态) 是 "disabled" （不可用）或没有指定 command 选项，则该方法无效
            select()	将 Radiobutton 控件设置为选中状态  

    @Checkbutton 复选框控件
        1.属性：
            属性	说明
            text	    显示的文本，使用 "\n" 来对文本进行换行。
            variable	1. 和复选框按钮关联的变量，该变量值会随着用户选择行为来改变（选或不选），即在 onvalue 和 offvalue 设置值之间切换，这些操作由系统自动完成
                        2. 在默认情况下，variable 选项设置为 1 表示选中状态，反之则为 0，表示不选中。
            onvalue	    通过设置 onvalue 的值来自定义选中状态的值。
            offvalue	通过设置 offvalue 的值来自定义未选中状态的值。
            indicatoron	默认为 True，表示是否绘制用来选择的选项的小方块，当设置为 False 时，会改变原有按钮的样式，与单选按钮相同
            selectcolor	选择框的颜色（即小方块的颜色），默认由系统指定
            selectimage	设置当 Checkbutton 为选中状态的时候显示的图片，若如果没有指定 image 选项，该选项被忽略
            textvariable	Checkbutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容，如果变量被修改，Checkbutton 的文本会自动更新
            wraplength	表示复选框文本应该被分成多少行，该选项指定每行的长度，单位是屏幕单元，默认值为 0
        2.方法：
            方法	属性
            desellect()	取消 Checkbutton 组件的选中状态，也就是设置 variable 为 offvalue
            flash() 	刷新 Checkbutton 组件，对其进行重绘操作，即将前景色与背景色互换从而产生闪烁的效果。
            invoke()	1. 调用 Checkbutton 中 command 选项指定的函数或方法，并返回函数的返回值
                        2. 如果 Checkbutton 的state(状态)"disabled"是 （不可用）或没有指定 command 选项，则该方法无效
            select()	将 Checkbutton 组件设置为选中状态，也就是设置 variable 为 onvalue
            toggle()	改变复选框的状态，如果复选框现在状态是 on，就改成 off，反之亦然      
            
                                
'''  # Radiobutton/Checkbutton

from tkinter import *

win = Tk()
win.geometry('400x180')
win.iconbitmap('logo.ico')

v = IntVar()
v.set(0)


def select():
    # strings = '您选择了' + str(v.get())
    strings = site[v.get()-1][0]
    label.config(text=strings)


# 使用variable参数来关联IntVar()的变量v
site = [('Radiobutton控件示例1', 1),
        ('Radiobutton控件示例2', 2),
        ('Radiobutton控件示例3', 3),
        ('Radiobutton控件示例4', 4)]
for sel, num in site:
    radio_button = Radiobutton(win, text=sel, variable=v, value=num, command=select)
    radio_button.pack(anchor='w')

# Radiobutton(win, text='Radiobutton控件示例1', fg='blue', font=('微软雅黑', '12', 'bold'),
#             variable=v, value=0).pack(anchor='w')
# Radiobutton(win, text='Radiobutton控件示例2', fg='blue', font=('微软雅黑', '12', 'bold'),
#             variable=v, value=2).pack(anchor='w')
# Radiobutton(win, text='Radiobutton控件示例3', fg='blue', font=('微软雅黑', '12', 'bold'),
#             variable=v, value=3).pack(anchor='w')
# Radiobutton(win, text='Radiobutton控件示例4', fg='blue', font=('微软雅黑', '12', 'bold'),
#             variable=v, value=4).pack(anchor='w')

label = Label(win, font=('微软雅黑', '15', 'bold'), fg='#43CD80')
label.pack(side='bottom')

label1 = Label(win,font=('微软雅黑', '15', 'bold'), fg='#43CD80')
label1.pack()

check1 = Checkbutton(win, text='checkbutton示例1', font=('微软雅黑', '15', 'bold'), fg='#43CD80')
check2 = Checkbutton(win, text='checkbutton示例2', font=('微软雅黑', '15', 'bold'), fg='#43CD80')
check3 = Checkbutton(win, text='checkbutton示例3', font=('微软雅黑', '15', 'bold'), fg='#43CD80')
# 将第一个复选框annual的variable值设置为onvalue=1，便是选中状态
check1.select()
# 取消第一个复选框的选中状态
# check1.toggle()
check1.pack(anchor='w')
check2.pack(anchor='w')
check3.pack(anchor='w')
win.mainloop()
