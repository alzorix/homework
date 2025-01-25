
digits = list()

with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":

        digits.append(int(line))
        line = file.readline().strip()
min_ysl_3 = min(digits) % 3
max_ysl_7 = max(digits) % 7

#UPD:Когда проверял,сам запутался.ВСЁ было верно
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
#1415 199020 -  ответ
