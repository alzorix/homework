from turtle import *
speed(5000)
tracer(0)
x = 4
k = 10
for z in range(3):
    forward(3*x*k)
    right(90)

forward(x*k)
right(90)

forward(2*x*k)
left(90)

forward(x*k)
left(90)

forward(2*x*k)
right(90)

forward(x*k)

penup()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3,"blue")

#алгебраическая прогрессия n(2a1 + d(n-1) )/2 = S


# 27n^2 -n -800 000 = 0 Ничего хорошего не получается




done()