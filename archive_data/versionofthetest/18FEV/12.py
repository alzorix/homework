def naslosh(s,v):
    return  v in s
def zamenit(s:str,v,w):
    return s.replace(v,w,1)

for  n in range(7,100):

    line = ">" + "0"*19 + "1"*n + "2" * 19
    while naslosh(line,">1") or naslosh(line,">2") or naslosh(line,">0"):
        if naslosh(line,">1") :
            line = zamenit(line,">1","22>")
        if naslosh(line,">2") :
            line = zamenit(line,">2","2>")
        if naslosh(line,">0") :
            line = zamenit(line,">0","1>")
    ssum = 0
    for x in line:
        if x != ">":
            ssum+=int(x)
    line = str(ssum)

    if line[-1] == line[-2]:
        print(n)
        exit()