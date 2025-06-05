import turtle
from  turtle import *
screensize(2000,2000)
tracer(0)
left(90)
pendown()

right(90)
k = 10

for _ in range(7):
    right(45)
    forward(11*k)
    right(45)
penup()
for x in range(-10,10):
    for y in range(-30,10):
        goto(x*k,y*k)
        dot(3,"blue")

done()
#113