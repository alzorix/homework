from turtle import *
k = 15
penup()
goto(-3*k,-4*k)
pendown()
left(90)

right(30)
tracer(0)

for x in range(10):
    forward(14*k)
    right(120)
penup()

for x in range(-20,0):
    for y in range(-20,0):
      dot(3,"blue")
      goto(x*k,y*k)
      dot(3, "blue")




done()
#6 с линиеми и 4 без