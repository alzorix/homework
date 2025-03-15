from turtle import *

'''Повтори 10 [
  Сместиться на (6, 15) 
  Сместиться на (-5, -5) 
  Сместиться в (2, 2) 
  Сместиться на (-1, -10)'''

k  = 20
tracer(0)
for x in range(10):
    goto(xcor()+ 6*k,ycor() + 15*k)
    goto(xcor() -5*k, ycor() -5*k)
    goto(2*k,  2*k)
    goto(xcor() -1*k, ycor() -10*k)

penup()
for x in range(-10,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot("3","blue")



done()
