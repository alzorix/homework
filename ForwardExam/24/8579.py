'''Текстовый файл состоит не более чем из 107 символов и содержит только
 буквы латинского алфавита и десятичные цифры.
 Найдите максимальную длину подстроки, которая начинается и
  заканчивается цифрами разной чётности,
 но при этом не содержит внутри других цифр. В ответе укажите длину найденной строки.'''
with open("24_8579.txt") as file:
    line = file.readline().strip()

chet = "02468"
nechet = "13579"

ans = list()
local_ans = 0
start = None
end = None
for bukva in line:
    if bukva.isdigit():
        if start == None:
            start = bukva
        else:
            end = bukva
            if (start in chet and end in nechet) or (start in nechet and end in chet):
                ans.append(local_ans+2)
            local_ans = 0
            start = end
            end = None
    else:
        local_ans += 1
print(max(ans))
#49+
#Вот такой и должна быть задача