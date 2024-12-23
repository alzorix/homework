def zamenit(s:str,v,w):
    return s.replace(str(v),str(w),1)
def nasloh(s:str,v):
    return str(v) in s
s = "9"*136
while nasloh(s,"22222") or nasloh(s,"9999"):
    if nasloh(s,"22222"):
        s = zamenit(s,"22222","99")
    else:
        s = zamenit(s,"9999","2")

print(136 - s.count("9"))