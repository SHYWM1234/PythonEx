import time as t
#line = input()
line = "8/11"
a = line.split("/")
up = int(a[0])
down = int(a[1])
list1=[]
i=1
sum=0
while(True):
    i=i+1
    if(round(sum+1/i - up/down, 15)==0):
        list1.append("1/"+str(i))
        print(list1)
        break;
    elif(sum+1/i <up/down):
        sum =sum + 1/i
        list1.append("1/"+str(i))
        print(list1)
    else:
        continue
    
print("===============")
print("+".join(list1))
