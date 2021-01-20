#cal shuixian
def shuixian (n) :
    baiwei = n // 100
    shiwei = (n % 100) // 10
    gewei = (n % 10)
    cal = baiwei ** 3 + shiwei ** 3 + gewei ** 3
    if cal == n :
        return True
    else :
        return False

a = 100
s = list()
while a < 1000 :
    if shuixian (a) :
        s.append ( str(a) )
    a += 1
print(','.join(s))
