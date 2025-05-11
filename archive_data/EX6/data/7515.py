from turtle import *

k = 10
speed(500)
screensize(3000,3000)
tracer(0)
right(90*3)
for x in range(3):
    forward(7*k)
    right(90)
    forward(12*k)
    right(90)

penup()

forward(4*k)
right(90)
forward(6*k)
left(90)

pendown()

for x in range(4):
    forward(83*k)
    right(90)
    forward(77*k)
    right(90)

penup()
for y in range(-150,60):
    for x in range(-150, 100):
        goto(x*k,y*k)
        dot(3,"blue")

done()