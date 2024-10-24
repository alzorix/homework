print(2*3*5*7*11*13*17*19*23)
print(2**3*3*5*7*11*13*17*19)
print(2**7*3*5*7*11*13*17)
print(2**9)
print(2*3**3*5*7*11*13*17*19)
from math import sqrt


#  - макс 15
def SEARCHDELALL(x):
    delList= list()


    sx = int(sqrt(x))
    for i in range(1,sx+1):
        if x % i == 0:


                delList.append( i)

                if i != x // i:

                        delList.append(x // i)
    return delList


min = float("inf")




for a1 in range(1,15):
    for a2 in range(0, 15):
        for a3 in range(0, 15):
            for a4 in range(0, 15):
                for a5 in range(0, 15):
                    for a6 in range(0, 15):

                             c = 2**    a1  *3**    a2  *5**    a3  *7**    a4  *11**    a5  *13**    a6
                             if len(SEARCHDELALL(c)) == 512:


                                if min > int(c):

                                    min = c
                                    print("############################")
                                    print(True,f"Получилось: {c}",f"Мин число:: {min}")
                                    print(" ")


