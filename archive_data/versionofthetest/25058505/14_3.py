line_ = 7**170 + 7**100
def absolute_solver(num):
    F = list()
    while num !=0:
        F.append(str(num% 7))
        num = num//7
    F.reverse()
    return "".join(F)
for x in range(2030,0,-1):
    line= line_
    line = line-x
    if absolute_solver(line).count("0") ==71:
        print(x)
        exit()
