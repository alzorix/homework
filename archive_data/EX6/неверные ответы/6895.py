from turtle import *
x = 3
k = 10
speed(500)
tracer(0)
for z in range(4):
    forward(3*x*k)
    right(90)
penup()
forward(x*k)
right(90)
forward(x*k)
pendown()
for z in range(4):
    forward(x*k)
    left(90)
penup()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3,"blue")

#такая же прогрессия :/

done()