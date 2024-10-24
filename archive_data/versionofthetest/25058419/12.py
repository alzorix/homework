def nashlos(v,l):
    return v in l
def zamenit(v,w,l:str):
    return  l.replace(v,w,1)

line = "9"*68

while nashlos("22222",line) or nashlos("9999",line):
    if nashlos("22222",line):
        line = zamenit("22222","99",line)
    else:
        line = zamenit("9999", "29", line)
print(line.count("9"))
#3