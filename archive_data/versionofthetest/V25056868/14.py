
def absolute_solver(bum):
    F = list()
    while bum !=0:
        F.append(str(bum%3))
        bum = bum // 3
    F.reverse()
    return "".join(F)



for x in range(2031,0,-1):
    line = 3**100 -x
    if absolute_solver(line).count("0") == 5:
        print(x)
        break
#2024