
all_elemets = set()

with open("26_15341.txt") as file:
    kolvo_kordji = int(file.readline().strip())

    line = file.readline().strip()
    while line !="":
        line = int(line)
        all_elemets.add(line)
        line = file.readline().strip()
    file.close()
all_elemets = list(all_elemets)
all_elemets.sort()
#print(all_elemets,kolvo_kordji)
all_elemets.reverse()
last  = -1
tort = list()

for i in all_elemets:
    if abs(last - i) >=8:
        last = i
        tort.append(i)
print(len(tort),min(tort))
#1198 54