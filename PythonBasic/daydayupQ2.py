#daydayupQ2
def daydayup (dayfactor) :
    day0 = 1.0
    for i in range (365) :
        if i % 7 in [0 , 6] :
            day0 = day0 * (1 - dayfactor)
        else :
            day0 = day0 * (1 + dayfactor)
    return day0
dayfactor = 0.01
day365 = daydayup (dayfactor)
print ("每天进步/退步{:.2f}%，周末休息时候，365天进步{:.2f}".format (dayfactor * 100 , day365))
