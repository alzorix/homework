with open("2650") as file:
    chislo_t = int(file.readline().strip())

    line = file.readline().strip()
    check = list()
    skidka =0
    while line!="":
        check.append(int(line))
        if int(line) > 200:
            skidka+=1

        line = file.readline().strip()


    check1 = check.copy()

    check.sort()
    skidka = skidka//2

    for i in range(len(check)):
        if check[i] > 200 and skidka !=0:
            t =check[i] - check[i] * 0.3

            maxx =  check[i]

            check[i] = t

            skidka -=1
        else:
            if skidka ==0:
                break




    print(sum(check),maxx)#464631.3 602 =>464632 602


