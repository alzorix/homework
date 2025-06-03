all_el_tort = set()
with open("26_16335.txt") as file:
    kolvo = file.readline().strip()
    line = file.readline().strip()

    while line !="":
        all_el_tort.add(int(line))
        line = file.readline().strip()
all_el_tort = list(all_el_tort)
all_el_tort.sort()
all_el_tort.reverse()
l= -1
tort = list()
for i in all_el_tort:
    if abs(l-i) >=4:
        l = i
        tort.append(i)
print(len(tort),min(tort))
#2172 50