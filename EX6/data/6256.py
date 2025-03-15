
from math import sqrt
from  turtle import *
k = 10
speed(1)
penup()
for x in range(2):
    forward(10*k)
    right(90)
    forward(20*k)
    right(90)
penup()
forward(4*k) ### имеет значение  только это
right(90)
forward(3*k) ###имеет значение  только это
left(90)
pendown()
for x in range(2):
    forward(70*k)
    right(90)
    forward(80*k)
    right(90)

print(sqrt(4**2 + 3**2))
done()
#5