import tkinter
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams["font.family"] = "Arial"

def readAtxtFile(dir1, str1) :
    try:
        f = open(dir1 + str1, "r")
    except Exception as e:
        print("文件" +dir1+ str1 + "不存在")
        listHeader = []
    else:
        print("文件"+dir1 + str1+ "读入成功")
        f1 = open("temp.txt", "w")
        txtheader = f.readline()
        for line in f.readlines() :
            f1.write(line)
        f.close()
        f1.close()
        listHeader = txtheader[:-1].split(" ")
        while '' in listHeader:
            listHeader.remove('') #删除列表中的所有空元素
    finally:
        pass
    return listHeader

def getTitle(str1) : 
    fileName = str1[: -4]
    title = fileName.split("_")
    if title[0] == "OWF" :
        title[0] = "Wave force "
    elif title[0] == "ODisp" :
        title[0] = "Displacements "
    elif title[0] == "OVel" :
        title[0] = "Velocities "
    elif title[0] == "OAcl" :
        title[0] = "Accelerations"
    else :
        print("error whatever")
    title[1] = "at T = " + str(int(title[1])) + " s"
    title[2] = "and H = " + str(round(0.1*int(title[2]), 1)) +" m"
    return " ".join(title)

def getLengend(param):
    legend1 = []
    for i in param :
        if i == 0 :
            legend1.append("纵荡(Surge)")
        elif i == 1 :
            legend1.append("横荡(Sway)")
        elif i == 2 :
            legend1.append("垂荡(Heave)")
        elif i == 3 :
            legend1.append("横摇(Roll)")
        elif i == 4 :
            legend1.append("纵摇(Pitch)")
        elif i == 5 :
            legend1.append("艏摇(Yaw)")
        elif i == 6 :
            legend1.append("水平(Horizontal)")
        else :
            print("ERR! \n-> File header information error")
    return legend1
def getYLabel(str1) :
    fileName = str1[: -4]
    yMeans = fileName.split("_")
    if yMeans[0] == "OWF" :
        return "Fw(N)"
    elif yMeans[0] == "ODisp" :
        return "Displacements(m)"
    elif yMeans[0] == "OVel" :
        return "V(m/s) "
    elif yMeans[0] == "OAcl" :
        return "Accelerations(m/s2)"
    else :
        return "error whatever"
    
def plotLegendOfFreeDegree(dir1, str1, param) : #param is a list
    listH = readAtxtFile(dir1, str1)
    if len(listH) == 0 :
        return
    elif len(param) > len(listH)-1 :
        print("parameter list is too long")
        return
    else :
        for i in range(len(param)) :
            if param[i] > len(listH)-2 :
                print("some parameter ERROR")
                return
        data = np.loadtxt("temp.txt")
        for i in range(len(param)) :
            plt.plot(data[:, 0], data[:, param[i]+1])
        plt.title(getTitle(str1))
        plt.xlabel("Time(s)")
        plt.ylabel(getYLabel(str1))
        plt.legend(getLengend(param), prop = {"family" : "SimHei"})
        plt.show()

def startPlot() :
    plt.close()
    selected = []
    try :
        selected.append( listb1.curselection()[0])
        selected.append( listb2.curselection()[0])
        selected.append( listb3.curselection()[0])
        selected.append( listb4.curselection()[0])
        selected.append( listb5.curselection())
    except :
        print("参数不足，无法出图")
    else:
        dirName = getDir(selected[0])
        fileName = getFileName(selected[1], selected[2], selected[3])
        plotLegendOfFreeDegree(dirName, fileName, selected[4])

def getDir( j ) :
    degree = round(eval(list1[j]))
    baiwei = str(degree // 100)
    shiwei = str((degree //10) %10)
    gewei = str(degree % 10)
    return "Out_time_" + baiwei + shiwei + gewei + "/"

def getFileName(i , j , k) :
    if k == 0 :
        str1 = "ODisp_"
    elif k ==1 :
        str1 = "OVel_"
    elif k == 2 :
        str1 = "OAcl_"
    elif k == 3 :
        str1 = "OWF_"
    else :
        str1 = "Selected ERR motion param"
    period = round( eval(list3[j]) )
    p_shiwei = str(period // 10)
    p_gewei = str(period % 10)
    str2 = p_shiwei + p_gewei 

    height = round( eval(list2[i]) * 10 )
    h_gewei = str( height // 10 )
    h_xiaoshu = str (height % 10)
    str3 = h_gewei + h_xiaoshu

    return str1 + str2 + "_" + str3 + ".TXT"

def getList( j ) :
    f1 = open("./Input/DATIND02.TXT", "r")
    for i in range(j):
        string = f1.readline()
    f1.close()
    list0 = string.split(" ", maxsplit=len(string)-1)
    while("" in list0) :
        list0.remove("")
    return list0

list1 = getList(7)
list2 = getList(5)
list3 = getList(9)
list4 = ['位移 (Displacements)', '速度 (Velocities)', '加速度 (Accelerations)', '力 (Wave force)']
list5 = ['纵荡 (Heave)', '横荡 (Sway)', '垂荡 (Heave)', '横摇 (Roll)', '纵摇 (Pitch)', '艏摇(Yaw)']

root = tkinter.Tk()
root.geometry("1000x600")
root.title("绘制时间历程曲线")
Label1 = tkinter.Label(root, text = "选择入射角度")
Label2 = tkinter.Label(root, text = "选择波高")
Label3 = tkinter.Label(root, text = "选择周期")
Label4 = tkinter.Label(root, text = "选择运动量(或力)")
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
listb2.grid(row = 1, column=1)
listb3.grid(row = 1, column=2)
listb4.grid(row = 1, column=3)
listb5.grid(row = 1, column=4)

button1 = tkinter.Button(root, text="我选好了，开始绘图", command = startPlot)
button1.grid(row=3, column=0,padx=20, pady=5)

root.mainloop()                 # 进入消息循环



