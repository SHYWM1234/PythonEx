import tkinter

def getSelected() :
    selected = []
    try :
        selected.append( listb1.curselection()[0])
        selected.append( listb2.curselection()[0])
        selected.append( listb3.curselection()[0])
        selected.append( listb4.curselection()[0])
        selected.append( listb5.curselection())
    except :
        text1.insert('0.0', '\n')
        text1.insert("0.0", "参数不足，无法出图")
    else:
        text1.insert('0.0', '\n')
        text1.insert("0.0", selected)

list1 = ['0.0','30.0','60.0','90.0','120.0','150.0']
list2 = ['1m','3m','5m','7m']
list3 = ['3.0s','4.0s','5.0s','6.0s','7.0s','8.0s']
list4 = ['CSS','jQuery','Bootstrap']
list5 = ['C','python','php','html','SQL','java']

root = tkinter.Tk()
root.geometry("950x450")
Label1 = tkinter.Label(root, text = "选择入射角度")
Label2 = tkinter.Label(root, text = "选择波高")
Label3 = tkinter.Label(root, text = "选择周期")
Label4 = tkinter.Label(root, text = "选择运动量(力)")
Label5 = tkinter.Label(root, text = "选择自由度(按住Ctrl可多选)")


Label1.grid(row=0, column=0)
Label2.grid(row=0, column=1)
Label3.grid(row=0, column=2)
Label4.grid(row=0, column=3)
Label5.grid(row=0, column=4)

listb1 = tkinter.Listbox(root, exportselection=0)          #  创建列表组件
listb2 = tkinter.Listbox(root, exportselection=0)
listb3 = tkinter.Listbox(root, exportselection=0)
listb4 = tkinter.Listbox(root, exportselection=0)
listb5 = tkinter.Listbox(root, exportselection=0, selectmode = "extended")

for item in list1:                 # 第一个小部件插入数据
    listb1.insert("end",item)
 
for item in list2:              # 第二个小部件插入数据
    listb2.insert("end",item)

for item in list3:                 # 第三个小部件插入数据
    listb3.insert("end",item)

for item in list4:                 # 第四个小部件插入数据
    listb4.insert("end",item)

for item in list5:                 # 第五个小部件插入数据
    listb5.insert("end",item)
 
listb1.grid(row = 1, column=0)
listb2.grid(row =1, column=1)
listb3.grid(row = 1, column=2)
listb4.grid(row = 1, column=3)
listb5.grid(row = 1, column=4)

button1 = tkinter.Button(root, text="我选好了，开始绘图", command = getSelected)
button1.grid(row=3, column=2,padx=20, pady=5)

text1 = tkinter.Text(root, height=3)
text1.grid(row = 4, column =0,columnspan=5)
root.mainloop()                 # 进入消息循环



