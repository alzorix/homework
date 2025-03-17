from turtle import *
tracer(0)
screensize(3000,3000)
k = 10
for x in range(3):
    forward(27*k)
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
for x in range(-30,30):
    for y in range(-30,30):
        dot(3,"blue")
        goto(x*k,y*k)

done() #83 * 77 + 27*12-30 = 6685