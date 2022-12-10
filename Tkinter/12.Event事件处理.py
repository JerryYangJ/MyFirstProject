'''
    @ 事件处理

    1.事件类型：
        <[modifier-]...type[-detail]>   
            -事件类型必须放置于尖括号<>内
            -type:必选项。事件类型，如键盘按键、鼠标单击
            -modifier：可选项。用于组合键定义，如Control、Alt.
            -detail：可选项。用于明确定义是哪一个键或按钮的事件。如1表示鼠标左键、2表示鼠标中键、3表示鼠标右键

        -键盘事件：
            <KeyPress-字母>/<KeyPress-数字>	按下键盘上的某一个字母或者数字键
            <KeyRelease>	释放键盘上的按键
            <Return>	回车键，其他同类型键有<Shift>/<Tab>/<Control>/<Alt>
            <Space>	空格键
            <UP>/<Down>/<Left>/<Right>	方向键
            <F1>...<F12>	常用的功能键
            <Control-Alt>	组合键，再比如<Control-Shift-KeyPress-T>，表示用户同时点击 Ctrl + Shift + T
        -鼠标事件：
            事件码	说明
            <ButtonPress-1>	单击鼠标左键，简写为<Button-1>，后面的数字可以是1/2/3，分别代表左键、中间滑轮、右键
            <ButtonRelease-1>	释放鼠标左键，后面数字可以是1/2/3，分别代表释放左键、滑轮、右键
            <B1-Motion>	按住鼠标左键移动，<B2-Motion>和<B3-Motion>分别表示按住鼠标滑轮移动、右键移动
            <MouseWheel>	转动鼠标滑轮
            <Double-Button-1>	双击鼠标左键
            <Enter>	鼠标光标进入控件实例
            <Leave>	鼠标光标离开控件实例
        -窗体事件：
            Visibility:当组件变为可视状态时触发
            Unmap：当组件由显示状态变为隐藏状态时触发
            Map：当组件由隐藏状态变为显示状态时触发
            Expose：当组件从原本被其他组件遮盖的状态中暴露出来时触发
            FocusIn：当组件获得焦点时触发
            FocusOut:当组件失去焦点时触发
            Configure：当改变组件大小时触发，如拖拽窗体边缘
            Property：当窗体的属性被删除或改变时触发，属于Tk的核心事件
            Destroy：当组件被销毁时触发
            Activate：与组件选项中的state项有关，表示组件由不可用转为可用
            Deactivate：与组件选项中的state项有关，表示组件由可用转为不可用
    2.Event事件对象常用属性：
        属性	说明
        widget	发生事件的是哪一个控件
        x,y	相对于窗口的左上角而言，当前鼠标的坐标位置
        x_root,y_root	相对于屏幕的左上角而言，当前鼠标的坐标位置
        char	用来显示所按键相对应的字符
        keysym	按键名，比如 Control_L 表示左边的 Ctrl 按键
        keycode	按键码，一个按键的数字编号，比如 Delete 按键码是107
        num	1/2/3中的一个，表示点击了鼠标的哪个按键，按键分为左、中、右
        width,height	控件的修改后的尺寸，对应着 <Configure>事件
        type	事件类型    ？？？？？？？？？？？？？？？？？？
    3.事件绑定：
        -创建组件对象时指定：通过命名参数command指定事件处理函数。
        -实例绑定：调用组件对象实例方法bind()。参数：<event>类型；func处理函数（回调函数）
                 只有组件获取焦点后才能接收键盘事件，因此给控件绑定事件和回调函数后，需要使用focus_set()方法来获取焦点
                 unbind()可以解除绑定
        -标识绑定：tag_bind()
'''  # 事件处理

from tkinter import *


# 定义事件函数，必须使用event参数
def show_key(event):
    print(event.type)
    # 查看触发事件的按钮
    s = event.keysym
    # 将其显示在按钮控件上
    lb.config(text=s)
    bt['text'] = s


win = Tk()
win.config(bg='#87CEEB')
win.title('Event事件示例')
win.geometry('450x350+300+200')
win.iconbitmap('logo.ico')

# 添加一个按钮控件
lb = Label(win, text='请按键', fg='blue', font=('微软雅黑', 15))

# 给按钮绑定事件，按下任意键，调用事件处理函数（需要在英文状态下进行输入）
lb.bind('<Key>', show_key)

# 设置按钮获取焦点
lb.focus_set()
lb.pack()

# 通过command指定事件处理函数
bt = Button(win, command=show_key)
bt.pack()
win.mainloop()