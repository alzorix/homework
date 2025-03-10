from turtle import *

pendown()
k = 10
right(90*3)

for x in range(15): 
    forward(4*k)
    right(60)
penup()
speed(5000)
for y in range(1,20):
    for x in range(1,20):
        goto(x*k,y*k)
        dot(3,"blue")