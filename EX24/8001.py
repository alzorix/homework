'''(№ 8001) Текстовый файл 24-320.txt состоит не более чем из 106 символов и содержит только десятичные цифры
 и знаки равенства («=»). Определите максимальную длину последовательности вида «число1=число2=число3=...=число N»,
  в которой нет соседних знаков «=» и есть хотя бы одно шестизначное число, в котором все цифры стоят в порядке невозрастания.
   В ответе укажите количество символов. '''

with open("8001") as file:
    line = file.readline().strip()

clear_data = line.split("=")

data = list()

send = list()
#print(clear_data)


#Выполяем условие: последовательности вида «число1=число2=число3=...=число N», которой нет соседних знаков «=»

for x in (clear_data):




    #Добавляем числа до тех пор, не встретим ==
    if x !="":
        if x[0] == "0": #Посмотрел на старые задания и решил перепроверить на незначащие нули / Их тут нет
            print(x)
        send.append(x)


    else: # Если встретили == , то список с числами,которые принадлежат одной последовательности, добавляем в другой список


        if len(send)!=0:
            data.append(send)
            send = []

if len(send)!=0:
        data.append( send)








#print(data)

#Выполяем условие: есть хотя бы одно шестизначное число, в котором все цифры стоят в порядке невозрастания

def ysl(x: str):
    x = str(x)
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            return False
    return True



def BIG_kostil(fucking_posl:list):
    cuts = list()
    for id in range(len(fucking_posl)):
        if ysl(potential):
            print(1)







good_ans = list() #Список с длинами подходящих последовательностей

for s in data:




    to_ans_if_successful = sum(len(num) for num in s) + (len(s) - 1)  #В длине учитываем и кол-во знаков = между цифрами


    TRUE = False


    for f_if in s:
        f_if= int(f_if)
        len_f_if = len(str(abs(f_if)))
        f_if = str(f_if)
        if len_f_if  == 6:



            if ysl(f_if):

                    #print(f_if)
                    TRUE = True
                    break

        elif len_f_if  > 6: # Проверка на большие числа
            for z in range(len_f_if   -5):

                potential = f_if[z:z+6]

                if ysl(potential):
                    r = BIG_kostil(s)
                    print("блять")







    if TRUE:

            good_ans.append(to_ans_if_successful)

print(max(good_ans))



