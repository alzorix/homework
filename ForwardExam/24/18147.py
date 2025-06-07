''' файл состоит из символов, обозначающих знаки « + », « * » и цифры 7, 8, 9.
Определите максимальное значение,
которое является результатом вычисления непрерывной последовательности,
 являющейся корректным арифметическим выражением из нескольких целых неотрицательных чисел,
 между которыми отсутствует операция умножения.
В этом выражении никакие два знака арифметических операций не стоят рядом.'''
with open("24_18147.txt") as file:
    line = file.readline().strip()
    line = line.replace("**", "*")
    line = line.replace("*+", "*")
    line = line.replace("+*", "*")


from copy import  deepcopy

data = line.split("*")
ans = list()

for line in data:
    line = line.split("+")
    ANS_LOCAL = 0

    for chislo in line:
        if chislo != "":

            if chislo != "" and chislo[0] != "0":
                ANS_LOCAL+=int(chislo)
                ans.append(ANS_LOCAL)
            elif chislo == "0":
                ans.append(ANS_LOCAL)
                ANS_LOCAL.clear()
            elif  chislo[0] == "0":
                ans.append(ANS_LOCAL)
                ANS_LOCAL=0
                t = deepcopy(chislo)

                t = t.replace("7", "1")
                t = t.replace("8", "1")
                t = t.replace("9", "1")

                r = t.find("1")
                if r>0:
                    ANS_LOCAL = int(chislo[r::])

            else:

                ans.append(ANS_LOCAL)
                ANS_LOCAL=0
            ans.append(ANS_LOCAL)
ans.sort()
print(max(ans))
#89797978998877-
