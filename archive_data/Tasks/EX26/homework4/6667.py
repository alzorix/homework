with open("26-127.txt") as file:
    gnom_int = file.readline().strip()
    line = file.readline().strip()

    orders = list()

    kotli = [0]*int(gnom_int)

    while line !="":
        intline = int(line)

        orders.append(intline)
        line = file.readline().strip()
    orders.sort()

    count_fine_users = 0
    for time_start in orders:
        for x in range(len(kotli)-1): # гном выбирает свободный котел с наименьшим номером
            if time_start >= kotli[x]:
                kotli[x]= time_start+6

                F =0 #Кол-во гномов,которые стоят рядом с подошедшим гномом


                try:
                    if kotli[x-1] > time_start +1:
                        F +=1
                except IndexError: #В случае, если гном занял первый котел.
                    None

                if kotli[x + 1] > time_start + 1:
                        F += 1


                if F ==0: #Если с гномом никто не стоит
                    count_fine_users+=1

                break

for i in range(len(kotli)): #Выше мы заполнили минимальное кол-во котлов,здесь мы ищём ни разу не занятый котел.
    if kotli[i] == 0:
        need = i
        break

print(need,count_fine_users) #38 199 - 50%