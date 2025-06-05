def zamenit(s:str,v,w):
    return s.replace(v,w,1)
def nashloh(s,v):
    return v in s


for n in range(3,10_001):
    line = "1" + "9" * n

    while nashloh(line,"19") or nashloh(line,"399") or nashloh(line,"999") :
        if nashloh(line, "19"):
            line = zamenit(line,"19","9")
        if nashloh(line, "399"):
            line = zamenit(line,"399","91")
        if nashloh(line, "999"):
            line = zamenit(line,"999","3")

    t = sum(int(r) for r in line)

    if t ==33:
        print(n)
        exit()
        #46