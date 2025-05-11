from turtle import *
k = 10
speed(1)
tracer(0)
screensize(3000,3000)
for x in range(15):
    goto(xcor()  +10*k , ycor() +10*k  )
    goto(xcor() + 3*k, ycor() - 6*k)
    goto(xcor() - 9*k, ycor() + 3*k)

print(xcor()/10,ycor()/10)

penup()
for x in range(0,200):
    for y in range(0, 200):
        goto(x*k,y*k)
        dot(3,"blue")

done()
#не получается получить правильный ответ