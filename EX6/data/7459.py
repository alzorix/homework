from turtle import *

k = 10
speed(500)
screensize(3000,3000)
tracer(0)
right(90*3)
for x in range(4):
    forward(28*k)
    right(90)
    forward(26*k)
    right(90)

penup()

forward(8*k)
right(90)
forward(7*k)
left(90)

pendown()

for x in range(4):
    forward(67*k)
    right(90)
    forward(98*k)
    right(90)

penup()
for y in range(-150,60):
    for x in range(-150, 100):
        goto(x*k,y*k)
        dot(3,"blue")

done()
#380