from turtle import *

screensize(3000,3000)
tracer(0)
right(90*3)
k = 10
for x in range(2):
    forward(16*k)
    right(90)
    forward(9*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(11*k)
right(90)
pendown()

for x in range(2):
    forward(20*k)
    right(90)
    forward(8*k)
    right(90)

penup()

for y in range(-40,40):
    for x in range(-40, 40):
        goto(x*k,y*k)
        dot(3,"blue")

done()
#159 считал в уме