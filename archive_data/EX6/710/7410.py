from turtle import *

k = 1
speed(3)
screensize(3000,3000)

shape("turtle")

right(90*3)

right(45)


for x in range(10):

    right(45)
    forward(203*k)
    right(45)

penup()

backward(40*k)
right(45)


pendown()

for x in range(5):
    forward(20*k)
    left(90)


penup()
done()
#Можно это руками НЕ считать?