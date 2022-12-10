'''
    @布局管理控件
        Tkinter  还提供了几个常用的布局管理控件，比如 Frame 、LabelFrame 等，这些控件的主要作用是为其他控件提供载体，并将主窗口界面划分成多个区域，从而方便开发者对不同区域进行设计与管理

    Frame控件
        Frame 本质上也是一个矩形窗体，同其他控件一样也需要位于主窗口内。我们可以在主窗口内放置多个 Frame 控件，并且每个 Frame 中还可以嵌套一个或者多个Frame，从而将主窗口界面划分成多个区域。

        常用属性：
            属性	说明
            bg	设置 Frame 的背景颜色
            bd	指定 Frame 的边框宽度
            colormap	指定  Frame 组件及其子组件的颜色映射
            container	布尔值参数，若参数值为 True，则窗体将被用作容器使用，一些其他程序也可以被嵌入。
            cursor	指定鼠标在 Frame 上飘过的鼠标样式，默认由系统指定
            height/width	设置 Frame 的高度和宽度
            highlightbackground	指定当 Frame 没有获得焦点的时候高亮边框的颜色，通常由系统指定为标准颜色
            highlightcolor	指定当 Frame 获得焦点的时候高亮边框的颜色
            highlightthickness	指定高亮边框的宽度，默认值是 0
            padx/pady	距离主窗口在水平/垂直方向上的外边距
            relief	指定边框的样式，参数值 "sunken"，"raised"，"groove" 或 "ridge"，"flat"，默认为 "falt'
            takefocus	布尔值参数，默认为 False，指定该组件是否接受输入焦点（即用户通过 Tab 键将焦点转移上来）

    LabelFrame控件
        LabelFrame 控件也是一种容器类型的控件，它属于是 Frame 控件的变体，因此它们的属性选项大体相同。

    PanedWindow控件
        PanedWindow（窗格界面）也可以理解成一个特殊的 Frame 控件，它是 Tkinter 8.4 版本后新增的空间管理组件，其主要目的是为其他组件提供一个容器或者框架，从而实现以分块的形式对图形界面进行布局。
        与 Frame 控件不同， PanedWindow 允许用户自主地调整界面划分以及每块区域的大小。因此，当您需要让用户自己调节每块区域的大小时，就可以采用 PanedWindow 作为组件载体来进行界面的布局

        常用方法：
            方法	说明
            add(child)	添加一个新的子组件到窗格中语法格式 add(child,**option)，参数值 after、before、sticky
            forget(child)	删除一个子组件
            panecget(child, option)	获得子组件指定选项的值
            paneconfig(child, **options)	设置子组件的各种选项
            panes()	将父组件中包含的子组件以列表的形式返回
            sash_coord(index)	返回一个二元组表示指定分割线的起点坐标
            sash_place(index, x, y)	将指定的分割线移动到一个新的位置

    Toplevel控件
        Topleve 是一个顶级窗口控件（也被称为“子窗体”控件），同样类似于 Frame 控件， 不过该控件会脱离根窗口另行创建一个独立窗口，因此它的存在形式不同于上述其他容器。
        Toplevel 控件同样隶属于主窗口的子组件，只是存在形式特殊而已。Toplevel 是主窗口之外的弹出框窗口（通过事件来触发执行），在这个窗口内也可以包含其他组件。但需要注意，顶级窗口并不是必须位于窗口的顶部位置，之所以称其为顶级窗口，是因为相对于主窗口而言，Topleve 位于主窗口的上一层。

        Toplevel 控件拥有根窗口控件的所有方法和属性，同时它还拥有一些独有的方法：
            方法	说明
            deiconify()	在使用 iconify() 或 withdraw() 方法后，即窗口最小化和移除窗口后（只是看不见，并没销毁），使用该方法来显示该窗口
            frame()	返回一个系统特定的窗口识别码
            group(window)	将顶级窗口加入 window 窗口群组中，如果忽略该参数，将返回当前窗口群的主窗口
            iconify()	将窗口图标化（最小化），需要重新显示窗口，使用 deiconify() 方法
            protocol(name, function)	将回调函数 function 与相应的规则 name 绑定；
                                        1) name 参数可以是 "WM_DELETE_WINDOW"：窗口被关闭的时候；
                                        2) name 参数可以是 "WM_SAVE_YOURSELF"：窗口被保存的时候；
                                        3) name 参数可以是 "WM_TAKE_FOCUS"：窗口获得焦点的时候。
            state()	设置和获得当前窗口的状态，参数值 "normal"（正常状态），"withdrawn（移除窗口）"，"icon"（最小化）和 "zoomed"（放大）
            transient(master)	指定为 master 的临时窗口
            withdraw()	将窗口从屏幕上移除，只是移动到了窗口之外，并没销毁，需要重新显示窗口，使用 deiconify() 方法
'''