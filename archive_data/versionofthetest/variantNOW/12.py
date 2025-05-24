def zamenit(s:str,v:str,w:str):
    return s.replace(v,w,1)
def nash(s,v):
    return v in s

s = set()
for n in range(4,1000):
    stroka = "4" + "7"*n

    while nash(stroka,"444") or nash(stroka,"777"):
        if  nash(stroka,"777"):
            stroka = zamenit(stroka,"777","4")
        else:
            stroka = zamenit(stroka, "444", "7")

    summa = sum(int(x) for x in stroka)
    s.add(summa)
print(max(s))
#36
