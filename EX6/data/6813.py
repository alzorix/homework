from turtle import *
screensize(3000,3000)
tracer(0)
right(90*3)
k = 10
for x in range(3):
    left(90)
    for t in range(4):
        forward(5*k)
        right(90)
penup()
for y in range(-40,40):
    for x in range(-40, 40):
        goto(x*k,y*k)
        dot(3,"blue")

done()
# 56 - считается в уме