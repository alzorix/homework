from turtle import *

k = 10

goto(0,0)
dot(4,"red")
c = 0
while True:
    с = input()
    c+=1
    print(c)
    goto(xcor() + 4*k,ycor() +3*k)
    goto(xcor() -5*k, ycor() + 10*k)
    goto(xcor() + 6*k, ycor() -6*k)
    goto(xcor() -5*k, ycor() -8*k)


#13
