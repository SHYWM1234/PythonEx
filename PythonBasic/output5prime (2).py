# 请在...补充一行或多行代码

def prime(m):
    end = int(pow(m, 0.5) + 1)
    for i in range(2, end):
        if m%i == 0:
            return False
    else:
        return True

n = eval(input())
if n != int(n):  
    n = int(n) + 1
else: 
    n = int(n)  
count = 5
while count > 0:
    if prime(n):
        if count > 1:
            print(n, end=',')
        else:
            print(n)
        count -= 1
    n += 1
