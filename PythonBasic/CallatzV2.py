K=eval(input())
list=[]
k=0
for i in  range(K):
    list.append(input())
for a in list:
    a=eval(a)
    while a!=1:
        if a%2==0:
            a=a/2

            if 'a' in list:
                list.remove('a')
        elif a%2!=0:
            a=(3*a+1)/2

            if 'a' in list:
                list.remove('a')

for q in list:
    print(q)
