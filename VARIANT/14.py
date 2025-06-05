
def absolute_solver(num):
    F = list()
    while num != 0:
        F.append(str(num%7))
        num = num//7
    F.reverse()
    return "".join(F)
for x in range(2300,-1,-1):
    s = 7**350 + 7**150 - x
    s1 = absolute_solver(s)
    if s1.count("0") ==200:
        print(x)
        exit()
#2001