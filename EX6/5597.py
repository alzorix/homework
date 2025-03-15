from turtle import *

for x in range(20):
    goto(xcor()  +  10  ,ycor()  +   20 )
    goto(xcor() + 5 , ycor()   - 15)
    goto(xcor()   - 12, ycor()      - 9 )

from math import sqrt

#100
print(sqrt(xcor()*xcor() + ycor()*ycor()))