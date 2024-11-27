

def nashlos(line,v):
    v = str(v)
    return v in line
def zamenit(line,v,w):
    v = str(v)
    w = str(w)
    return line.replace(v,w,1)
count = 0
for i in range(123_456_794, 678_901_235):

    line = "1"*i
    while nashlos(line,111):
        start = line
        line = zamenit(line,111, 2)
        line = zamenit(line,222, 11)
        line = zamenit(line,1, 2)
        if start == line:
            break
    if line.count("2") == len(line):
        count+=1
print(count)

#Быстрее сделать ручками,да?