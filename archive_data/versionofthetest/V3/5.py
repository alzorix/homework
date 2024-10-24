def calc(num):
    F = list()
    while num !=0:
        F.append(str(num%4))
        num = num // 4
    F.reverse()
    return "".join(F)

for n in range(1,999):
    fon = calc(n)
    #print(fon,fon[-2::])
    if n %4 == 0:
        fon = fon + fon[-2::]
    else:
        fon = fon + calc((n % 4)*2)

    if int(fon,4) >=1025:
        print(n)
        break



