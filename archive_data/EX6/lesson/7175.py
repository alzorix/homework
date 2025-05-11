from  turtle import *
k = 10
hist = list()
penup()

def check():
    if xcor() in hist:
        dot(3,"white")
        hist.remove(xcor())
    else:
        dot(3,"black")
        hist.append(xcor())



for x in range(4):
    check()
    backward(2*k)
    for y in range(4):
        forward(3*k)
        check()
    check()
#goto(100000000000000,1000000000000000)
print(xcor()/k *16)
done()
