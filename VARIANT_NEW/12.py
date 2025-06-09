line = "1" + "8"*70

def nasloh(s:str,v:str):
    return v in s
def zamenit(s:str,v:str,w:str):
    return s.replace(v,w,1) #По условию не сказано как заменять. Написал как обычно
#Перепроверил разницы тут нет
while nasloh(line,"1"):
    if nasloh(line,"18"):
        line = zamenit(line,"18","88881")
    else:
        line = zamenit(line, "1", "8888")

print(line.count("8"))
#284