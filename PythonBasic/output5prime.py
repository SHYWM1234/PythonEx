# 连续输出指定数字之后的5个素数
import time
start = time.perf_counter()

def prime(m):
    if m == 2 :
        return False
    else :
        for i in range (2 , m) :
            if m % i == 0 :
                return True
                break
            else :
                continue
        else :
            return False
def outputprime (a) :
    num = a
    while prime(num) :
        num = num + 1
    return num

n = eval(input())
n1 = int(n)
for i in range (20) :
    if i ==19 :
        pri = outputprime(n1)
        print (pri , end = '')
        n1 = pri +1
    else :
        pri = outputprime(n1)
        print (pri , end = ' , ')
        n1 = pri +1

end = time.perf_counter()
print ('\n程序运行的总时间为' , end - start , 's')
str1 = time.ctime()
print ('现在的时间为', str1)
