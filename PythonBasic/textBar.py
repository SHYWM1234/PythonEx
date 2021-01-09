#textprobar
import time
scale = 50
print ("start".center (scale // 2 , "-"))
start = time.perf_counter()
for i in range (scale + 1) :
    str1 = "*" * i
    str2 = "." * (scale - i)
    end = time.perf_counter()
    dur = end - start
    print ("\r{:^3.0f}%[{}->{}]{:.2f}s".format(i*100/scale,str1,str2,dur) , end = "")
    time.sleep (0.1)
print ("\n" + "end".center (scale // 2 , "-"))