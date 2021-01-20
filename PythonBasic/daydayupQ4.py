#daydayupQ3
def daydayup (dayfactor) :
    day0 = 1.0
    for i in range (365) :
        if i % 7 in [0 , 6] :
            day0 = day0 * (1 - 0.01)
        else :
            day0 = day0 * (1 + dayfactor)
    return day0
dayf = 0.01
while daydayup (dayf) < 1.01 ** 365 :
    dayf += 0.001
print ("B君需要每天进步{:.3f}".format (dayf))
