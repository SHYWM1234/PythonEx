#day day up Q1
def daydayup (dayfactor) :
    day0 = 1.0
    for i in range (365) :
        day0 = day0 * (1 + dayfactor)
    return day0
dayfactor = 0.005
day365 = daydayup (dayfactor)
print ("每天进步{:.2f}%，365天进步为{:.2f}".format(dayfactor*100,day365))
