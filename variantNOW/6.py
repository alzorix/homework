import turtle
from turtle import *

screensize(2000,2000)
tracer(0)
coif = 10
left(90)

for x in range(5):
    forward(6*coif)
    right(90)
    forward(3*coif)
    forward(90)
penup()
forward(4 * coif)
right(90)
forward(2 * coif)
forward(90)
pendown()
for x in range(8):
    forward(8*coif)
    right(90)
    forward(5*coif)
    forward(90)
penup()
forward(4 * coif)
right(90)
forward(2 * coif)
forward(90)
pendown()
for x in range(4):
    forward(5*coif)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*coif,y*coif)
        dot(3,"blue")


done()
# 22 * 22 + 2*18 = 520