#print star

n = 10
for i in range(n) :
    s = '*' * (i  * 2 + 1)
    print ("{0:^{1}}".format(s,2*n-1))
