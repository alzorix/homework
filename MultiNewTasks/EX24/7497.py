'''(№ 7497) (ЕГЭ-2024) Текстовый файл 24-298.txt состоит не более чем из 106 символов и содержит только символы,
 обозначающие знаки «-», «*», и цифры 0, 7, 8, 9. Определите в прилагаемом файле максимальное количество идущих подряд
  символов, которые образуют математически правильную последовательность,
  в которую входят знаки «-» или «*» и натуральные числа без незначащих нулей. '''
with open("7497") as file:
    line = file.readline().strip()
    file.close()

# line = line.replace("7","1")
# line = line.replace("8","1")
# line = line.replace("9","1")

line = line.replace("-","*")

def ysl(num:str):
    last = -1
    for n in num:
        if last == -1:
            last = n
        else:
            if last <= n:
                None
            else:
                #print(num)
                return False
    return True

line = line.split("*")
print(line)

c = 0
local_c=0
for candidat in line:
    if ysl(candidat):

     if candidat != "" and (candidat[0] != "0" or candidat == "0"):

            local_c +=len(candidat) +1
            c = max(local_c - 1, c)
     elif  candidat != "" and candidat[0] == "0":
            c = max(local_c + 1, c)
            normal_bukva = min(candidat.find("1") , candidat.find("7") , candidat.find("8") , candidat.find("9"))
            if normal_bukva >-1:
                local_c = len(candidat[normal_bukva::]) +1
                c = max(local_c-1,c)
            else:
                local_c = 2
                c = max(local_c-1,c)

     else:
            local_c = 0
print(c)




