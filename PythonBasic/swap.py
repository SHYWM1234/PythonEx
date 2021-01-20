def swap( x , y ) :
    if x < y :
        t = x
        x = y
        y = t
    return x , y
a , b , c = 11,34,100
a , b = swap(a , b)
a , c = swap(a , c)
b , c = swap(b , c)
print (a , b, c)
