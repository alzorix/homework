with open("26-64.txt") as file:
    line = file.readline().strip().split()
    N = int(line[0])
    balance = int(line[1])
    line = file.readline().strip()
    A = list()
    B = list()
    C = list()
    D = list()
    E = list()
    all_need_ABCDE =list()
    while line!="":
        price,type = line.split()
        price = int(price)
        match type:
            case "A":
                A.append(price)
            case "B":
                B.append(price)
            case "C":
                C.append(price)
            case "D":
                D.append(price)
            case "E":
                E.append(price)
        all_need_ABCDE.append((price,type))
        line = file.readline().strip()


    all_need_ABCDE.sort(key= lambda x:x[0])
    count_max = 0

    for i in range(len(all_need_ABCDE)):
        price = all_need_ABCDE[i][0]
        if price <= balance:
            last = balance
            balance-=price
            count_max +=1

        else:
            break
    print(count_max) # максимальное кол-во товаров













    #
    # #Покупаем товары всех типов ,кроме B ,выполняя условие: Необходимо на выделенную сумму закупить как можно больше товаров пяти типов
    # balance -= min(A)
    # balance-= min(C)
    # balance-= min(D)
    # balance-= min(E)
    # print(balance)
    # B.sort()
    # print(B)
    # count = 4
    # #Выполняем условие:. Если можно разными способами купить максимальное количество пяти типов товаров, то нужно выбрать способ, при котором будет закуплено как можно больше товаров типа B.
    # for i in B:
    #         if balance >= i: #Тратим деньги максимально эффективно
    #             balance-=i
    #             count+=1
    #         else:
    #             break
    # print(count,balance) #Ответ неверный :(   85 187