for N in range(1,1000):
    binN= bin(N)[2::]

    if binN.count("1") % 2 == 0:


        binN = "101"+binN[3::]+ "0"


    else:
        s = binN
        binN = "11" + binN[:-2] + "10"
        print(s,binN)

    if int(binN,2) >=68:
        print(N)
        break
#Где ошибка? Получается ответ 16,заместо 19