import turtle as t
t.penup( )
t.seth(-90)
t.fd(160)
t.pendown( )
t.pensize(20)
t.colormode(255)
for j in range(10) :
    t.speed(100)
    t.pencolor(25*j , 10*j , 10*j)
    t.seth(130)
    t.fd(220)
    t.circle(-80 , 230)
    t.seth(100)
    t.circle(-80 , 230)
    t.fd(220)
