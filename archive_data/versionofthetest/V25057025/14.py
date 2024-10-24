number_not_good = 6**2030 + 6 ** 100

def absolutesolver(num):
    F = list()
    while num !=0:
        F.append(str(num%6))
        num = num//6
    F.reverse()
    return "".join(F)



s = list()
for x in range(1,2031):
    number = number_not_good-x
    s.append(absolutesolver(number).count("0"))
print(max(s))
#1934