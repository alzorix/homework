from turtle import *
k = 30
screensize(4000,4000)
tracer(0)
for x in range(2):
    forward(20*k)
    right(90)
    forward(35*k)
    right(90)
right(90)
x = 28
forward(x*k)
right(90)
forward(3*k)
for x in range(4):
    left(90)
    forward(6*k)


penup()
for x in range(-20,20):
    for y in range(-40,20):
        dot(3,"blue")
        goto(x*k,y*k)
done()
#не очень понятно,что делать с x,но max кол-во точек 28 - это правильный ответ