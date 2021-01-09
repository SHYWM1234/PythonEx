str = input()[2:]
ls = list(str)
#print(ls)
num=0
for i in range(len(ls)):
    
    char = ls[len(ls)-i-1]
#    print(char)
    if (char in ['1','2','3','4','5','6','7','8','9','0']):
        num = num + eval(char)*pow(16,i)
    elif(char == 'A'):
        num = num + 10*pow(16,i)
    elif(char == 'B'):
        num = num + 11*pow(16,i)
    elif(char == 'C'):
        num = num + 12*pow(16,i)
    elif(char == 'D'):
        num = num + 13*pow(16,i)
    elif(char == 'E'):
        num = num + 14*pow(16,i)
    else:
        num = num + 15*pow(16,i)
print(num)
