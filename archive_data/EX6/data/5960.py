from turtle import *
speed(1)
pendown()
k = 10
from math import sqrt
goto(xcor() + 0 * k  ,ycor()+  12   * k)
goto(xcor() + 5 * k,ycor()+  -12  * k )# 25 + 144
goto(xcor() -10 * k ,ycor()+  0 * k  ) # 10
goto(xcor() +  5 * k ,ycor()+ 12 * k   ) #25+ 144
goto(xcor() +   0 * k,ycor()+   4 * k ) # 4
goto(xcor() +   3 * k,ycor()+   -4 * k ) # 9 + 16
goto(xcor() +  -6 * k ,ycor()+   0 * k ) # 6
goto(xcor() +  3 * k ,ycor()+  4 * k  )
print((sqrt(25+144) + 10 + sqrt(25+144) ) - (sqrt(9+16) + 3 + 4))
done()
#24