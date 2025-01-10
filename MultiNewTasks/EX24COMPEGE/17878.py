'''

№ 17878 Демоверсия 2025 (Уровень: Сложный)

Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков арифметических операций «–» и «*» (вычитание и умножение).
 Определите максимальное количество символов в непрерывной последовательности, которая является корректным арифметическим выражением
  с целыми неотрицательными числами.
В этом выражении никакие два знака арифметических операций не стоят рядом,
 в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака.
В ответе укажите количество символов.'''
with open("24_17878.txt") as f:
    line = f.readline().strip()

line = line.replace("6","1")
line = line.replace("7","1")
line = line.replace("8","1")
line = line.replace("9","1")
line = line.replace("-0","#")

#line = line.replace("-","*")

# в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака. - это запрет на  replace "-" ?

line = line.split("*")
#print(line)

mp = 0
lp = 0

def ysl(num:str):
    if "#" in num:
        temp = list()
        ind = list()

        maxx = list()
        flag = True
        last = -1

        chet = -1
        for x in num:
            chet += 1
            temp.append(x)
            if x == "#":
                if flag:
                    last = chet
                    flag = False
                else:
                    maxx.append(chet - last)

                    last = chet

                ind.append(chet)

        ind.sort()
        if len(maxx) != 0:
            return (False,ind[0],len(temp) - ind[-1],max(maxx)  )
        else:
            return (False,ind[0],len(temp) - ind[-1],0 )#Не забываем,что под # -0,а 0*223 может быть
    return (True,0,0,0)





for c_l in line:
    if c_l !="" and ( c_l[0] !="0" or c_l == "0"):
        Q,start,end,maxx = ysl(c_l)
        if Q:
            lp +=len(c_l) +1
            mp = max(mp,lp-1)
        else:
            lp += start
            mp = max(mp, lp)

            lp = end
            mp = max(mp, lp)

            mp = max(mp, maxx)

    elif c_l !="" and c_l[0] !="0":
        Q,start,end,maxx = ysl(c_l)
        if Q:
            mp = max(mp,lp+1)

            nice_index = c_l.find("1")
            if nice_index > -1:
                lp = len(c_l[nice_index::]) +1
                mp = max(mp,lp-1)
            else:
                lp = 2
                mp = max(mp, lp - 1)
        else:

            mp = max(mp,lp+1)

            nice_index = c_l.find("1")
            if nice_index > -1 and nice_index > start:
                lp = len(c_l[nice_index::]) +1
                mp = max(mp,lp-1)
            elif nice_index > -1 and nice_index < start:
                lp += start
                mp = max(mp, lp)

                lp = end + 1
                mp = max(mp, lp)

                mp = max(mp, maxx)
            else:
                lp = 2
                mp = max(mp, lp - 1)




    else:
        lp = 0
print(mp)
print(ysl("100#00#003"))

#Не получилось