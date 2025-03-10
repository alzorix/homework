from turtle import *

right(90*3)
k = 10
for x in range(5):
    for z in range(3):
        forward(4*k)
        left(90)
        forward(2*k)
    forward(2*k)
done()
# 14,при условии,что за квадраты мы считаем прямоугольники. Каждый квадрат прямоугольник,но не каждый прямоугольник квадрат