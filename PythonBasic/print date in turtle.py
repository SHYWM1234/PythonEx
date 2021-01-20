def gap () :
    turtle.penup()
    turtle.fd(5)
def drawline ( draw ) :
    gap()
    if draw :
        turtle.pendown ()
    else :
        turtle.penup ()
    turtle.forward(40)
    gap()
    turtle.right(90)
def drawnum (num) :
    if num in [ '2' , '3' , '4' , '5' , '6' , '8' , '9' ] : #第一段
        drawline (True)
    else :
        drawline (False)
    if num in [ '0' , '1' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ] : #第二段
        drawline (True)
    else :
        drawline (False)
    if num in [ '0' , '2' , '3' , '5' , '6' , '8' , '9' ] : #第三段
        drawline (True)
    else :
        drawline (False)
    if num in [ '2' , '6' , '8' , '0' ] : # 第四段
        drawline (True)
    else :
        drawline (False)
    turtle.left(90) #左转90度
    if num in [ '0' , '4' , '5' , '6' , '8' , '9' ] : #5
        drawline (True)
    else :
        drawline (False)
    if num in [ '0' , '2' , '3' , '5' , '6' , '7' , '8' , '9' ] : #6
        drawline (True)
    else :
        drawline (False)
    if num in [ '0' , '1' , '2' , '3' , '4' , '7' , '8' , '9' ] : #7
        drawline (True)
    else :
        drawline (False)
    turtle.right(180)
    turtle.penup()
    turtle.forward(30)
def drawdate(d) :
    turtle.color('red')
    for i in d[0:4] :
        drawnum(i)
    turtle.write('年' )
    turtle.color('green')
    turtle.forward(40)
    for i in d[4:6] :
        drawnum(i)
    turtle.write('月')
    turtle.color('blue')
    turtle.forward(40)
    for i in d[6:] :
        drawnum(i)
    turtle.write('日')
import turtle
import time
turtle.penup()
turtle.fd(-400)
turtle.pensize(5)
date= time.strftime('%Y%m%d',time.gmtime())
drawdate(date)
turtle.hideturtle()
