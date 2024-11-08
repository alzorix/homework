'''(№ 6676) (ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 106 символов и
содержит только заглавные буквы латинского алфавита и цифры. Определите
максимальную длину подстроки, которая может являться записью числа в
шестнадцатеричной системе счисления'''
with open("24.txt") as file:
    line = file.readline().strip()
    file.close()
alfabet = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
ansewers = list()
count =0
for bukva in line:
    if bukva in alfabet:
        if count ==0 and bukva == "0":
             count=0
        else:
            count +=1
    else:
        ansewers.append(count)
        count=0
print(max(ansewers))