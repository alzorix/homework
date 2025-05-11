from turtle import *
#shape("turtle")
speed(5)

screensize(2000,2000)
tracer(0)
m = 30
for x in range(2):
    forward(13 * m)
    right(90)
    forward(20 * m)
    right(90)
penup()
forward(8 * m)
right(90)
backward(3 * m)
left(90)
pendown()


for x in range(2):
    forward(16 * m)
    right(90)
    forward(8 * m)
    right(90)



penup()

for x in range(-30, 60):
    for y in range(-30, 60):
        goto(x * m, y * m)
        dot(4, "blue")



done()