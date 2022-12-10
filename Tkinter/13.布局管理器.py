'''
    @几何布局管理器： grid() 布局方法不能与 pack() 混合在一起使用
        -pack：采用块的方式组织组件，按照控件的添加顺序进行排列，灵活性差
            pack(option=value...)
                -side:停靠在父组件的那一边。top\bottom\left\right
                -anchor:八个方向。n\s\e\w\nw\sw\se\ne\center(默认值）
                -fill:填充空间。x\y\both\none
                -expand:扩展空间。0\1
                -ipadx\ipady:组件内部在x\y方向上填充的空间大小。单位c(厘米）\m（毫米）\i（英寸\p（打印点）
                -padx\pady:组件外部在x\y方向上填充的空间大小。
        -grid:采用表格结构的方式组织组件
            grid(option= value...)
                -sticky:组件紧贴所在单元格的某一边角。n\s\e\w\nw\sw\se\ne\center(默认值）
                -row:单元格行号
                -column:单元格列号
                -rowspan:行跨度
                -columnspan:列跨度
                -ipadx\ipady:组件内部在x\y方向上填充的空间大小。单位c(厘米）\m（毫米）\i（英寸\p（打印点）
                -padx\pady:组件外部在x\y方向上填充的空间大小。
        -place:允许指定组件的大小和位置
            place(option= value...)
                -x\y:绝对坐标
                -relx\rely：相对坐标
                -height\weidth:高度和宽度。像素
                -anchor:八个方向。n\s\e\w\nw\sw\se\ne\center(默认值）
'''  # 布局管理器

import tkinter as tk
# 几何布局grid()
win2 = tk.Tk()
win2.geometry('200x200+280+280')    # 280为初始化窗口所在的位置
win2.title('计算器示例')

l1 = tk.Button(win2, text='1', width=5, bg='yellow')
l2 = tk.Button(win2, text='2', width=5)
l3 = tk.Button(win2, text='3', width=5)
l4 = tk.Button(win2, text='4', width=5)
l5 = tk.Button(win2, text='5', width=5)
l6 = tk.Button(win2, text='6', width=5)
l7 = tk.Button(win2, text='7', width=5)
l8 = tk.Button(win2, text='8', width=5)
l9 = tk.Button(win2, text='9', width=5)
l0 = tk.Button(win2, text='0', width=5)
ld = tk.Button(win2, text='.', width=5)
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
l3.grid(row=0, column=2)
l4.grid(row=1, column=0)
l5.grid(row=1, column=1)
l6.grid(row=1, column=2)
l7.grid(row=2, column=0)
l8.grid(row=2, column=1)
l9.grid(row=2, column=2)
l0.grid(row=3, column=0, columnspan=2, sticky=('e' + 'w'))  # 跨两列，左右紧贴
ld.grid(row=3, column=2)
b1 = tk.Button(win2, text='我是随便放置的按钮')
b1.place(x=20, y=150)
# b1.place(anchor='nw')
win2.mainloop()