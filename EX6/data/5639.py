from turtle import *
screensize(3000,3000)
k = 50
speed(500)
tracer(0)
for x in range(4):
    for y in range(4):
        for z in range(4):
            for v in range(4):
                forward(3*k)
                right(120)
            forward(3*k)
        forward(3*k)
done()
#13
