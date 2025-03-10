from turtle import *
speed(500)

F = list()
k = 30
penup()
def check():
    if xcor() in F:
        F.remove(xcor())
        dot(3,"red")
    else:
        F.append(xcor())
        dot(3,"blue")




for x in range(27):
    forward(5*k)
    check()
    backward(3*k)
    check()
    backward(3*k)
done()
#6
