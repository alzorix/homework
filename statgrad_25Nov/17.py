
digits = list()

with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":

        digits.append(int(line))
        line = file.readline().strip()
min_ysl_3 = max(digits) % 3 #  от деления на 3 максимального элемента всей последовательности
max_ysl_7 = min(digits) % 7 #  от деления на 7 минимального элемента всей последовательности.
#Была ошибка наоборот
#Имена переменных не менял
def ysl3(number):
    return number % 3 == min_ysl_3

def ysl7(number):
    return number % 7 == max_ysl_7

pari = list()

for i in range(len(digits)-1):
    if ysl3(digits[i]) or ysl3(digits[i+1]):
        if ysl7(digits[i]) or ysl7(digits[i + 1]):
            pari.append(digits[i]+digits[i+1])
print(len(pari),max(pari))
#1415 199020 - старый ответ
#1467 197700 - новый ответ