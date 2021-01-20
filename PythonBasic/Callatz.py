#Callatz
def odd(num) :
    if num%2 == 1 :
        return True
    else :
        return False

def callatz( num ) :
    n = num
    step = 0
    while n !=1 :
        if odd(n) :
             n = (3*n + 1) /2
             step +=1
        else :
            n = n/2
            step +=1
    return step

def main() :
    c = eval( input("请输入数字：") ) 
    c = int(c)
    if c<1 or c>1000 :
        print("error")
    else:
        #pass
        print( "Callatz 次数为：{}".format(callatz(c) ))
main()
