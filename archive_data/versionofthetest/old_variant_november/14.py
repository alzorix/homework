number = 7*729**543 - 6*81**765 - 5*9**987 - 20

def trnasformator9(num) -> str:
    F = list()
    while num !=0:
        F.append(str(num%9))
        num = num //9
    F.reverse()
    return "".join(F)
print(trnasformator9(number).count("8"))