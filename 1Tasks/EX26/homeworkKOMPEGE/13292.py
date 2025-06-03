with open("26_13292.txt") as f:
    line = f.readline().strip()
    N, K = line.split()

    int_detail = int(N)
    int_mest = int(K)

    storage = [0]* int_mest
    line = f.readline().strip()

    all_detail = list()
    while line !="":
        dlina = int(line)
        all_detail.append(dlina)
        line = f.readline().strip()
    all_detail.sort()

    #print(N, K)
    start_index =0
    end_index = int_mest -1

    check_full = int_mest
    #детали с четными длинами располагают в левой части хранилища, с нечетными - в правой

    for i in range(len(all_detail)):
        if check_full !=0:
            if all_detail[i] % 2 == 0:
                storage[start_index] =all_detail[i]
                last = start_index
                start_index+=1
                check_full -=1

            else:
                storage[end_index] = all_detail[i]
                last = end_index
                end_index -= 1
                check_full -= 1
        else:

            break



print(last +1,sum(storage[last+1::])) # Места в хранилище пронумерованы слева направо, начиная с единицы


#415 1473503