
F = dict()



with open("3750") as lines:
    line = lines.readline().strip()
    for l in range(len(line)-2):
        if line[l] == line[l+2]:

            if line[l+1]  not in F:
                F[line[l+1]] = 1
            else:
                F[line[l + 1]]  +=1
print(F)
r = sorted(F)


naib = 0
naibbukva = 0


for i in r:
    if (F[i] > naib):
        naib = F[i]
        naibbukva = i
print(f"{naibbukva}{naib}")