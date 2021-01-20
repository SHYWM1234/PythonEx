#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    s = input ()
    n = s.split(',')
    return list (map(eval , n) )

def mean(numbers):  #计算平均值
    n = len(numbers)
    i = 0
    sum1 = 0.0
    while i < n :
        sum1 = sum1 + numbers[i]
        i += 1
    return sum1 /n
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    num = sorted(numbers)
    n = len (numbers)
    if n % 2 == 1 :
        med = num [(n-1)//2]
    else :
        med = ( num[n//2] + num[n//2-1] ) / 2
    return med
    
n =  getNum() #主体函数
m =  mean(n)
de = dev (n , mean(n))
med = median(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m , de , med))
