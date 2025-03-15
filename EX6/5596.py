from turtle import *
speed(1)

k = 10

for x in range(2): # 6*2
    goto(xcor() + 6*k, ycor()+ 2*k)
    goto(xcor() + 0*k, ycor()-2*k)

for x in range(3): # 2*2 * 1.5
    goto(xcor() + 2*k, ycor()-1*k)
    goto(xcor() -2*k, ycor()-1*k)

for x in range(6): # 6*6
    goto(xcor() -2*k, ycor()+ 1*k)

print(6*6 + 2*2*1.5 + 6*2)

done()
#54