sum = 0
for i in range(1,966+1):
    sum = sum + (-1)**(i%2 +1) * i
print(sum)

'''
n = 0
for i in range (966 + 1) :
    if i % 2 == 1 :
        n = n + i
    else :
        n = n - i 
print (n)
'''