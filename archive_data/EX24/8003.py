'''(№ 8003) Текстовый файл 24-320.txt состоит не более чем из 106 символов и содержит только десятичные цифры и знаки равенства («=»).
 Определите максимальную длину последовательности вида «число1=число2=число3=...=число N»,
  в которой нет соседних знаков «=» и есть хотя бы одно пятизначное число,
   которое является квадратом простого целого числа.
   В ответе укажите количество символов. '''



with open("8003") as file:
    line = file.readline().strip()

clear_data = line.split("=")

data = dict()
id = 0
send = list()
#print(clear_data)


#Выполяем условие: последовательности вида «число1=число2=число3=...=число N»,
# которой нет соседних знаков «=»

for x in (clear_data):
    #print(x)



    if x !="":
        send.append(x)


    else:

        if len(send)!=0:
            data[id] = send
            send = []
            id += 1
if len(send)!=0:
        data[id] = send



#print(data)

#Выполяем условие:  есть хотя бы одно пятизначное число,
# которое является квадратом простого целого числа.






from math import sqrt

def its_simple(dig:int):
    recombinate = int(sqrt(dig))+1
    for x in range(2,recombinate):
        if dig% x == 0:
            return False

    return True

good_ans = list()

for x in data.items():
    s = x[1]


    to_ans_if_successful = sum(len(num) for num in s) + (len(s) - 1)
    #которой нет соседних знаков «=» / Мы их тут не учитываем
    TRUE = False


    for f_if in s:
        f_if= int(f_if)
        if len(str(abs(f_if)))  == 5:
            simple=   sqrt(f_if)


            if simple == int(simple):
                if its_simple(int(simple)):
                    #print(f_if)
                    TRUE = True
                    break

    if TRUE:
            good_ans.append(to_ans_if_successful)
print(good_ans)






