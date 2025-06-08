data = list()
with open("26_18967(1).txt") as file:
    N,K = map(int,file.readline().strip().split())
    #N — общее количество мест в гардеробе; K — количество людей
    line = file.readline().strip()

    while line !="":
        ID,start,kolvo = map(int,line.split())
        data.append((start,ID,kolvo))
        line = file.readline().strip()


data.sort()

current_occupied =0
IDs_in_kino = list()

dforf_toptop = 0
full_clothes = 0


for current_time in range(1441):
    if current_occupied == N:
        full_clothes +=1
    for chelovik in data:
        start,ID, kolvo = chelovik
        if start == current_time:
            if ID not in IDs_in_kino:

                if current_occupied < N:
                    current_occupied+=kolvo
                    IDs_in_kino.append(ID)
                else:
                    dforf_toptop+=kolvo

            else:
                IDs_in_kino.remove(ID)
                current_occupied -=kolvo
print(dforf_toptop,full_clothes)
#12933 320
#Всё неправильно