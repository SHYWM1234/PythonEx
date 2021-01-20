# calculate pi
from random import random
from time import perf_counter
darts = 1000 * 100
hits = 0
start = perf_counter ()
for i in range ( 1 , darts+1 ) :
    x , y = random () , random ()
    dis = pow (x , 2) + pow (y , 2)
    if dis < 1 :
        hits += 1
print ('圆周率π的近似值为：' , 4 *hits/darts)
print ('运行时间为：' , perf_counter() - start , 's')
