from  turtle import *
speed(2000)
tracer(0)
k = 30
screensize(20000,20000)
for x in range(777):
    forward(25*k)
    left(90)
    forward(34*k)
    left(90)
penup()
forward(12*k)
left(90)
forward(17*k)
right(90)
pendown()
for x in range(1997):
    forward(25*k)
    left(90)
    forward(17*k)
    left(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot("4","blue")





done()