import turtle
import time
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
def main() :
    c = eval(input())
    turtle.setup(800, 350, 200, 200)
    turtle.speed(10000)
    turtle.pensize(5)
    turtle.penup()
    turtle.fd(-300)
    turtle.hideturtle()
    for i in range(c) :
        turtle.goto(0,0)
        drawnum(str(c - i))
        turtle.write('秒' )
        time.sleep(1)        
        turtle.clear()
main()
