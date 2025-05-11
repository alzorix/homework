from turtle import *

penup()
speed(1)
k = 10
tracer(0)
for x in range(-5,50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3,"blue")

goto(0,0)
pendown()
x = 5

for f in range(x):
    for z in range(4):
        forward(30*k)
        right(90)

    penup()
    forward(5*k)
    right(90)
    forward(5*k)
    pendown()
    right(270)



done()
#не понял,что от меня хотят:
#При каком значении параметра k нарисованная на поле траектория Черепахи пройдет несколько раз ровно через 20 точек?

#5