from turtle import *
x = 4
k = 10
for f in range(x):
    for z in range(4):
        forward(30*k)
        right(90)
        penup()
    forward(5*k)
    right(90)
    forward(5*k)
    pendown()
    right(270)
done()
#не понял,что от меня хотят:
#При каком значении параметра k нарисованная на поле траектория Черепахи пройдет несколько раз ровно через 20 точек?