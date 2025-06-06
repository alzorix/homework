''' файл состоит из символов, обозначающих знаки « + », « * » и цифры 7, 8, 9.
Определите максимальное значение,
которое является результатом вычисления непрерывной последовательности,
 являющейся корректным арифметическим выражением из нескольких целых неотрицательных чисел,
 между которыми отсутствует операция умножения.
В этом выражении никакие два знака арифметических операций не стоят рядом.'''
with open("24_18147.txt") as file:
    line = file.readline().strip()
    line = line.replace("**", "+")
    line = line.replace("*+", "+")
    line = line.replace("+*", "+")


from copy import  deepcopy
data = line.split("+")
ans = list()

for LOCAL_line in data:
    LOCAL_line = LOCAL_line.strip("*")
    ANS_LOCAL = list()
    for chislo in LOCAL_line:

            if chislo != "" and (chislo[0] != "0"):
                ANS_LOCAL.append(chislo)
                ans.append(ANS_LOCAL)
            elif chislo == "0":
                ans.append(ANS_LOCAL)
                ANS_LOCAL.clear()
            elif  chislo[0] == "0":
                ans.append(ANS_LOCAL)
                ANS_LOCAL.clear()
                t = deepcopy(chislo)

                t = t.replace("7", "1")
                t = t.replace("8", "1")
                t = t.replace("9", "1")

                r = t.find("1")
                if r>0:
                    ANS_LOCAL.append(chislo[r::])

            else:

                ans.append(ANS_LOCAL)
                ANS_LOCAL.clear()
print(ans)

def calculate(clust):
    fist = ""
    two = ""
    oper = None
    F = True
    for chislo in clust:
        if chislo.isdigit() == True:

            if F:
                fist = fist + chislo
            else:
                two = two + chislo
        else:
            if F:
                F = False
                oper = chislo
            else:
                fist = str(eval(fist + oper + two))
                two = ""
                oper = chislo
    return fist
ansewers = [calculate(p) for p in ans]
print(max(ansewers))
#999999988777