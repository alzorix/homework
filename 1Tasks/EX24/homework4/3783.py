
mincount = float("inf")
minstr = ""




with open("3783") as file:
    line = file.readline().strip()
    while line != "":
        count = 0
        for l in range(len(line)-1):
            if ord(line[l]) < ord(line[l+1]) and abs(ord(line[l]) - ord(line[l+1])) <2:
                count+=1

        if count < mincount and count != 0:
            minstr = line
            mincount = count
        line = file.readline().strip()
print(mincount,minstr)


FUNNY = dict()
for i in minstr:
    if i not in FUNNY:
        FUNNY[i] = 1
    else:
        FUNNY[i] += 1
print(FUNNY)
a = (sorted(FUNNY))

a.reverse()


max_test = max(FUNNY.values())
for i in a:
    if FUNNY.get(i) == max_test:
        need_str = i
        break

final_count = 0

with open("3783") as file:
    line = file.readline().strip()
    while line !="":
        for i in line:
            if need_str == i:
                final_count +=1


        line = file.readline().strip()

print(need_str,final_count)
#W 38473