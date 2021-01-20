#e1.TempConvert.py
TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['c' , 'C'] :
    f = ((eval(TempStr[ :-1]) * 1.8) + 32)
    print ('转换后的温度值为：{:.2f}F'.format(f) )
elif TempStr[-1] in ['f' ,'F'] :
    c = ((eval(TempStr[ :-1]) - 32 ) / 1.8)
    print ('转换后的温度值为：{:.2f}C'.format(c) )
else :
    print ('您输入的格式有误！')
