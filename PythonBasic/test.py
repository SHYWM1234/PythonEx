import time as t
line = input()
a = line.split("/")
up = int(a[0])
down = int(a[1])
list1 = []
i = 1
sum = 0
while(True):
    i =i +1
    if(abs(sum + 1/i - up/down) < 1e-10):
        list1.append("1/" + str(i))
        print(list1)
        break
    elif(sum + 1/i < up/down):
        sum = sum+1/i
        list1.append("1/"+str(i))
        print(list1)
    else:
        continue
print("_________________")
print("+".join(list1))
