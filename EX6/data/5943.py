from turtle import *

k = 10

for x in range(2):
    forward(8*k)
    right(90)
    forward(6*k)
    right(90)
penup()
backward(2*k)
right(90)
backward(4*k)
left(90)

pendown()

for z in range(2):
    forward(5*k)
    right(90)
    forward(6*k)
    right(90)
penup()
tracer(0)
for x in range(-5,50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3,"blue")

done()
#57