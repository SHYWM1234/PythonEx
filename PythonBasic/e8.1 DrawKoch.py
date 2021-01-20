#e8.1DrawKoch.py
import turtle
def Koch(size , n) :
    if n == 0 :
        turtle.fd(size)
    else :
        for angle in [ 0 , 60 , -120 , 60 ] :
            turtle.left(angle)
            Koch(size / 3 , n-1)
def main() :
    turtle.setup(800 , 400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300 , -50)
    turtle.pendown()
    turtle.pensize(2)
    Koch(600 , 2) #科赫雪花0阶长度 ， 阶数
    turtle.hideturtle()
main()
