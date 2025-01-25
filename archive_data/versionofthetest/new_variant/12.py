def naslosh(s:str,v:str):
    return v in s

def zamenit(s:str,v:str,w:str):
    return s.replace(v,w,1)

for n in range(4,10_000):

    line = "1" + "2" * n
    while naslosh(line,"12") or naslosh(line,"322") or naslosh(line,"222"):
        if naslosh(line,"12"):
            line = zamenit(line,"12","2")
        if naslosh(line,"322"):
            line = zamenit(line,"322","21")
        if naslosh(line,"222"):
            line = zamenit(line,"222","3")
    ss = 0
    for x in line:
        ss += int(x)
    if ss == 15:
        print(n)
        exit()
#37