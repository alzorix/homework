def nashlos(s:str,v):
    return v in s
def zamenit(s:str,v,w):
    return  s.replace(v,w)

for n in range(7,101):
    line = ">" + "0" * 19 + "1" * n

# возможно листок ввиду большого перебора
