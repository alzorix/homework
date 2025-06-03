with open("26-135.txt") as file:
    all_clients = int(file.readline().strip())

    line = file.readline().strip()
    orders = dict()
    while line!="":
        riad,seat = line.split()
        riad = int(riad)
        seat = int(seat)

        if riad not in orders:
           orders[riad] = {seat}

        else:
            orders[riad].add(seat)
        line = file.readline().strip()
riads = list(orders.keys())
riads.sort()
riads.reverse()
count_good_seat = 0
good_riad = None
for rev_index in riads:
    FIST = True
    line = list(orders[rev_index])

    line.sort()
    print(line)

    for i in range(len(line)-1):
        if FIST:
            FIST = False
        else:
            if abs(line[i-1] - line[i])-1 ==5 and  abs(line[i] - line[i+1])-1 ==5: # почему нужен -1
                if good_riad == None:
                    good_riad = rev_index
                count_good_seat+=1
print(good_riad,count_good_seat)


