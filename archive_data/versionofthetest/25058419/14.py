I = 4**644 +4**322+16**35 - 64**3

def solver(num):
    F = list(
    )
    while num !=0:
        F.append(str(num%4))
        num = num//4
    F.reverse()
    return "".join(F)
print(solver(I).count("3"))
#61