'''Текстовый файл состоит из десятичных цифр и заглавных букв латинского
 алфавита. Onределите в этом файле последовательность идущих подряд символов,
  представляющих собой запись максимального кратного пяти 15-ричного числа.
   В ответе запишите индекс (номер) последнего символа (последней значащей цифры),
    которой заканчивается запись этого числа в прилагаемом файле.
    Нумерация символов в текстовом файле начинается с нуля.
Примечание. Латинские буквы А, В, C, D, E - цифры из алфавита 15-ричной системы счисления.'''

with open("24_22359(1).txt") as file:
    line = file.readline().strip()
import copy
source = copy.deepcopy(line)
BLACKLINE= "QWRTYUIOPSFGHJKLZXVNM"
new_line = list()
for x in line:
    if x not in BLACKLINE:
        new_line.append(x)
    else:
        new_line.append("!")
line = "".join(new_line)
data = line.split("!")

def normalize(num):
    line = str(num)
    if line[0] == "0":

        line = line.replace("2","1")
        line = line.replace("3", "1")
        line = line.replace("4", "1")
        line = line.replace("5", "1")
        line = line.replace("6", "1")
        line = line.replace("7", "1")
        line = line.replace("8", "1")
        line = line.replace("9", "1")
        line = line.replace("A", "1")
        line = line.replace("B", "1")
        line = line.replace("C", "1")
        line = line.replace("D", "1")
        line = line.replace("E", "1")
        r = line.find("1")
        if r >0:

            return str(num)[r::]
        else:
            return ""
    return str(num)
def ysl(num):
    num = str(num)
    while int(num,15)%15!=0 and len(num)!=1:
        num = num[:len(num)-1]
    return num
ans = list()
for candidat in data:
    if candidat !="":
        candidat = normalize(candidat)
        if candidat !="":
            #print(candidat)
            candidat = ysl(candidat)
            if candidat !="":
                ans.append((len(candidat),candidat))

print(source.rfind(max(ans)[1])+ len(max(ans)[1])-1) #счёт уже с нуля,НО в rfind это первый индекс строки
#7432968

