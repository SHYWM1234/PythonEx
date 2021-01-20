#print bar
import time
scale=100
print('start'.center(scale//2,"-"))
for i in range(11):
    print("\r{:^4.0f}".format(i*10),'%','[','*'*(i),'->','.'*(10-i),']',end='')
    time.sleep(0.1)

