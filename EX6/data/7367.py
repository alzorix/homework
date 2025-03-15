from turtle import *
k = 10
penup()

F = list()
def check():
    if xcor() in F:
        dot(3, "red")
        F.remove(xcor())
    else:
        dot(3, "blue")
        F.append(xcor())
for x in range(7):
    for y in range(2):
        forward(3*k)
    check()
    backward(4*k)
    check()
done()
#4