from turtle import *
speed(500)
tracer(0)
right(90*3)
screensize(3000,3000)
penup()
k = 10
for x in range(10):
    right(120)
    forward(10*k)
pendown()

for x in range(7):

    forward(15*k)
    right(90)

for x in range(5):
    right(60)
    forward(20*k)
    right(30)

penup()

for x in range(-100,100):
    for y in range(-100,100):
        dot(3,"blue")
        goto(x*k,y*k)
done()
#74