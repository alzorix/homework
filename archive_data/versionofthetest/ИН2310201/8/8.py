'''Сколько существует 11-значных девятеричных чисел, в записи которых
не встречается цифра 0, любые две соседние цифры имеют разную чётность,
и никакая цифра не повторяется больше 4 раз?'''


chet = [ "2",   "4",  "6",    "8"]
nechet = [  "1",   "3",   "5",  "7"]
#S = "+".join("qwertyuiopa")

sus = 0
for q in nechet:
    for w in chet:
        for e in nechet:
            for r in chet:
                for t in nechet:
                    for y in chet:
                        for u in nechet:
                            for i in chet:
                                for o in nechet:
                                    for p in chet:
                                        for a in nechet:
                                            S = q+w+e+r+t+y+u+i+o+p+a
                                            if S.count("1")>4 or S.count("2")>4 or S.count("3")>4 or S.count("4")>4 or  S.count("5")>4 or S.count("6")>4 or  S.count("7")>4 or S.count("8")>4:
                                                None
                                            else:
                                                sus +=1
print(sus) #4100400


nechet = [ "2",   "4",  "6",    "8"]
chet = [  "1",   "3",   "5",  "7"]
#S = "+".join("qwertyuiopa")

sus1 = 0
for q in nechet:
    for w in chet:
        for e in nechet:
            for r in chet:
                for t in nechet:
                    for y in chet:
                        for u in nechet:
                            for i in chet:
                                for o in nechet:
                                    for p in chet:
                                        for a in nechet:
                                            S = q+w+e+r+t+y+u+i+o+p+a
                                            if S.count("1")>4 or S.count("2")>4 or S.count("3")>4 or S.count("4")>4 or  S.count("5")>4 or S.count("6")>4 or  S.count("7")>4 or S.count("8")>4:
                                                None
                                            else:
                                                sus1 +=1
print(sus1+ sus) #8200800

