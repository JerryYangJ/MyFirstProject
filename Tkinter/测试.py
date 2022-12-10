import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x350+200+200')
win.iconbitmap('./Tkinter/logo.ico')
# 在主窗口上添加一个frame控件
frame1 = tk.Frame(win)
frame1.pack()
# 在frame_1上添加另外两个frame， 一个在靠左，一个靠右
#左侧的frame
frame_left = tk.Frame(frame1)
tk.Label(frame_left,text='左侧标签1',bg='green',width=10,height=5).grid(row =0,column=0)
tk.Label(frame_left,text='左侧标签2',bg='blue',width=10,height=5).grid(row = 1 ,column =1)
frame_left.pack(side=tk.LEFT)
frame_right = tk.Frame(frame1)
tk.Label(frame_right,text='右侧标签1',bg='gray',width=10,height=5).grid(row = 0 ,column =1)
tk.Label(frame_right,text='右侧标签2',bg='pink',width=10,height=5).grid(row = 1 ,column =0)
tk.Label(frame_right,text='右侧标签3',bg='purple',width=10,height=5).grid(row= 1,column=1)
frame_right.pack(side=tk.RIGHT)
win.mainloop()