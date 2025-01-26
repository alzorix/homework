'''Текстовый файл состоит из десятичных цифр, а так же знака точки и знака & (амперсанд).
 Определите максимальное количество символов в непрерывной последовательности,
  которая является выражением вида четырехзначное вещественное число&четырехзначное вещественное число (например, 1234.56&2345.09874).
   В записи чисел отсутствуют незначащие (ведущие) нули.
В ответе укажите количество символов'''
with open("24_18597.txt") as f:
    line = f.readline().strip()


smart_start = 0
#А как? Идей пока нет

line = line.split("&")

len_max_line = 0

for line_index in range(len(line)-1):
    last_tochka = line[line_index]
    fist_tochka = line[line_index+1]

    posledovatelnost = 0



    if "." in last_tochka and "." in fist_tochka:
        #last_tochka
        last_tocka_podstroka = last_tochka.split(".")
        last_podstroka = last_tocka_podstroka[-2]
        if len(last_podstroka) >=4 and last_tocka_podstroka[-1] != "":
            ysl_last = last_podstroka[-4::]

            if ysl_last[0] != "0":
                posledovatelnost +=5 + len(last_tocka_podstroka[-1]) + 1 # точка и амперсенд

        #fist_locka
        fist_tocka_podstroka = fist_tochka.split(".")
        fist_podstroka = fist_tocka_podstroka[0]

        if len(fist_podstroka) ==4 and fist_tocka_podstroka[1] != "":

            if fist_podstroka[0] != "0":
                posledovatelnost +=4 +1 + len(fist_tocka_podstroka[1]) # 4  + точка + ост цифры

                len_max_line = max(len_max_line,posledovatelnost)
print(len_max_line)



