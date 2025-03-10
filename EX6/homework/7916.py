from turtle import *
k = 10
right(90*3)
speed(3000)
for x in range(8):
    forward(16*k)
    right(90)
    forward(22*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(5*k)
left(90)
pendown()
for x in range(8):
    forward(52*k)
    right(90)
    forward(77*k)
    right(90)

penup()

for y in range(-10,50):
    for x in range(-10,50):
        goto(x*k,y*k)
        dot(3,"blue")

done()