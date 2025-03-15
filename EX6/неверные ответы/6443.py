from turtle import *
speed(5000)
right(90*3)
k = 10
forward(2)
tracer(0)
x = 100

for z in range(5):
    forward(x*k)
    right(90)
    forward(3*k)
    right(90)
    forward(x * k)
    left(90)
    forward(1 * k)
    left(90)
backward(2*k)





penup()
goto(0,0)
pendown()
goto(500,0)



penup()
for x in range(0,50):
    for y in range(0, 50):
        goto(x*k,y*k)
        dot(3,"blue")


done()

# x - 10 точек 25000/10 = 2500 2500-1 = 2499
# Откуда берутся ещё 10 точек? ( правильный ответ 2498)