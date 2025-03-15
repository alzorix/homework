from turtle import *

k = 10
speed(500)
screensize(3000,3000)
tracer(0)
for x in range(10):
    forward(22*k)
    right(90)
    forward(16*k)
    right(90)

penup()

forward(1*k)
right(90)
forward(1*k)
left(90)

pendown()

for x in range(10):
    forward(72*k)
    right(90)
    forward(79*k)
    right(90)

penup()
for y in range(-100,100):
    for x in range(-50, 100):
        goto(x*k,y*k)
        dot(3,"blue")

done()