line = 3* 3125**8 + 2*625**7 -4*625**6 + 3*125**5 -2*25**4-2025

def absolute_solver(num):
    F = list()
    while num !=0:
        F.append(str(num% 25))
        num = num//25
    F.reverse()
    return "".join(F)
print(absolute_solver(line).count("0"))