import time
#num=input('请输入正确的18位身份证号')
num = '371327199711070000'
age=int(num[6:10])
age
print('你出生于'+num[6:10]+'年'+num[10:12]+'月'+num[12:14]+'日')
year = time.ctime()
print('你今年' , eval(year[ -4 : ]) - eval(num[6:10] ) , '岁')
