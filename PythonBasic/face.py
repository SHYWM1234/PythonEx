#from tkinter import *
import tkinter as t
# 导入tkinter模块的所有内容

root = t.Tk()
s="深海夜未眠，\n请扫码添加！"

# 创建一个文本Label对象
w = t.Label(root , text=s, justify=t.LEFT, padx=50)
#w.pack(side=LEFT)   # 致命 textlabel 在初识框 中的位置
w.pack()
# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象（支持gif格式的图片）
photo = t.PhotoImage(file="18.gif")
imgLabel = t.Label(root, image=photo)  # 绑定在初始旷上面 
#imgLabel.pack(side=RIGHT)  # 指明 图片位置
imgLabel.pack()
t.mainloop()
