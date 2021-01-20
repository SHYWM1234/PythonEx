import math

a=eval(input('请输入第一个边长值'))
b=eval(input('请输入第二个边长值'))
c=eval(input('请输入两边长的夹角角度值'))
third=math.sqrt(math.pow(a,2)+math.pow(b,2)-2*a*b*math.cos(c*math.pi/180))
print('第三边长为：',third)
