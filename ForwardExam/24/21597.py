with open("24_21597.txt") as file:
    line = file.readline().strip()


line = line.replace("6","!")
line = line.replace("7","!")
line = line.replace("8","!")
line = line.replace("9","!")

line = line.replace("**","!")
line = line.replace("-*","!")
line = line.replace("*-","!")
line = line.replace("--","!")
line = line.replace("1","1")
line = line.replace("2","1")
line = line.replace("3","1")
line = line.replace("4","1")
line = line.replace("5","1")
data = line.split("!")
ans = list()


ans = list()

for six_line in data:

    id_line = 0
    six_line = six_line.strip("*-") #01-011-00111*01
    if six_line != "":
        current_dlina = 0
        current_six_line = six_line.replace("-","*")
        current_data = six_line.split("*")
        for chislo in current_data:
            id_line +=len(chislo)
            if chislo != "" and (chislo[0] != "0" or chislo == "0"):
                current_dlina += len(chislo) +1
                ans.append((current_dlina - 1,six_line[:id_line-1]))
            elif  chislo[0] == "0":
                ans.append((current_dlina +1,six_line[:id_line]))
                current_dlina =0
                r = chislo.find("1")
                if r>0:
                    current_dlina = len(chislo[r::])+1
                else:
                    ans.append((current_dlina - 1,six_line[:id_line+1]))
                    current_dlina = 0

            else:
                ans.append((current_dlina-1,six_line[:id_line-1]))
                current_dlina =0

ans.sort(reverse=True)

print(ans[1])

for c,line in ans:


    chislaandoperation = [p for p in line]
    fist = ""
    two = ""
    oper = None
    F = True
    for chislo in chislaandoperation:
        if chislo.isdigit() == True:

            if F:
                fist = fist + chislo
            else:
                two = two + chislo
        else:
            if F:
                F = False
                oper = chislo
            else:
                fist = str(eval(fist+oper+two))
                two = ""
                oper = chislo

        if fist == eval(chislo):
            print(c)
            exit()

#Опять долго  писал и ничего не работает