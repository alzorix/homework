alfabet = [ "1","2","3","4","5","6","7","8","9","0",              "A", "B", "C", "D", "E", "F"]

all_ = list()
count = 0

with open("6676") as lines:
    line = lines.readline().strip()
    for l in line:
        if l in alfabet:
            count+=1
        else:
            all_.append(count)
            count = 0

    if count!=0:
        all_.append(count)
print(max(all_))