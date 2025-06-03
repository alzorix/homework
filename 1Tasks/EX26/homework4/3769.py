with open("26-53.txt") as file:
    chisla = int(file.readline().strip())

    line = file.readline().strip()
    all = set()
    terra = list()
    while line!="":
        line = int(line)
        if line %2 !=0:
            terra.append(line)
        all.add(line)
        line = file.readline().strip()

    file.close()

ansewers = list()
test = set()
for i1 in terra:
    for i2 in terra:
        if i1 not in test and i2 not in test:
         if i1 != i2:
            srARIF = (i1+i2)//2
            if srARIF in all:
                test.add(i1)
                test.add(i2)
                ansewers.append(srARIF)
print(len(ansewers),max(ansewers)) # Про надобность test = set нигде не сказанно ОТВЕТ:38 884877115

