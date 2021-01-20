#textprobar
import time
scale = 51
print ("执行开始".center (scale // 1 , "="))
for i in range (scale) :
    time.sleep(0.1)
    str1 = "*" * i
    str2 = "." * (scale -1 - i)
    print ("\r{:^3}% [{}->{}]".format (i *2 , str1 , str2) , end = "")
print ("\n" + "执行结束".center (20 , "="))
cc = input ("请输入任何字符以结束程序")
