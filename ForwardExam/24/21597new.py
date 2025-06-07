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

ansewers = list()
#Переписал,но снова пришёл к выводу,что нужен id,и срезы соответсвенно. Только они у меня снова неверные
data = line.split("!")
for local in data:
    local = local.strip("-*")
    if ("*" in local) or ("-" in local):
        THIS_line = local
        start = 0
        id = 0
        local_ans = list()

        THIS_line = THIS_line.replace("-","*")

        L_data = THIS_line.split("*")

        for candidat in L_data: #2323+234*02312
                if candidat != "" and (candidat[0] != "0" or candidat == "0"):
                    id +=len(candidat)-1 +1 #-1 индексация с 0, +1 из-за знака
                    local_ans.append(local[start:id-0])#вычетаем знак
                elif candidat != "" and candidat[0] == "0":
                    id += 1 #добавляем только 0,так как + уже учитывется
                    local_ans.append(local[start:id+1]) #+1 из-за особоенности среза


                    positions = [candidat.find(d) for d in "12345"]
                    normal_bukva = min([p for p in positions if p != -1], default=-1)
                    if normal_bukva > -1:
                        start += id + normal_bukva

                        id = id + len(candidat)-1 +1 #-1 индексация с 0; +1 из-за знака
                        local_ans.append(local[start:id])#вычетаем знак

                    else:

                        start = id + len(candidat)-1 +1#Фактически сбос
                        id = id + len(candidat)-1 +1#Фактически сбос

                else:

                    id +=1 #возможно нужно +2
                    start = id
        local_ans.append(local[start:id+1])
        ansewers.append(local_ans)
print(ansewers)
#В ansewers встречаются такие строки
# ['10', '10-', '10-4', '10-4*'] ,
# по идеи в  '10-4*' знака * быть не должно.
# Должна быть либо 4 либо другая цифра после *.
# Где ошибка?

def ysl(line:str): #На вход по очереди передаём ['10', '10-', '10-4', '10-4*'],
    # тем самым обеспечивая перебор с двух сторон
    if "*" in line and "-" in line:
        if line.rfind("*") < line.find("-"):
            return True
        else:
            while "*" in line and "-" in line:
                if line.rfind("*") < line.find("-"):
                    return True
                line = line[1::]
            return False

    else:
        if "*" in line or "-" in line:
            return True
        else:
            return False
