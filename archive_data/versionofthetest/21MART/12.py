def nashlos(s:str,v):
    return v in s
def zamenit(s:str,v,w):
    return  s.replace(v,w,1)


line = "1"*81
while nashlos(line,"111") or nashlos(line,"88888"):
        if nashlos(line,"111") :
            line = zamenit(line,"111","88")
        if nashlos(line,"88888") :
            line = zamenit(line,"88888","8")

print(line)