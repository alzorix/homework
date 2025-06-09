alfabet = "0123456789AB"
chet = "02468A"
nechet="13579B"

from  itertools import product
c = 0
s = set()
for x in product(alfabet,repeat = 5):
    line = "".join(x)
    if line not in s:
        s.add(line)
        if line.count("3") ==1:
            F = True
            for id in range(len(line)-1):
                if (line[id] in chet and line[id+1] in nechet) or (line[id] in nechet and line[id+1] in chet):
                    None
                else:
                    F = False
            if F:
                c+=1
print(c)
#4860
