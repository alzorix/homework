'''
(№ 3155) Текстовый файл 24-s2.txt состоит не более чем из 106 заглавных латинских букв.
 Определите символ, который чаще
 всего встречается в файле сразу после буквы A.
 В ответе запишите сначала этот символ, а потом сразу (без разделителя)
  сколько раз он встретился после буквы А. Если таких символов несколько,
   нужно вывести тот, который стоит раньше в алфавите.
   Например, в тексте ABCAABADDD после буквы A два раза стоит B,
   по одному разу – A и D. Для этого текста ответом будет B2.
'''

C = dict()


with open("3155") as lines:
    line = lines.readline().strip()
    for l in  range(0,len(line)-1):
        if line[l] =="A":
            if line[l+1]  not in C:
                C[line[l+1]] = 1
            else:
                C[line[l + 1]]  +=1
sorted_C = sorted(C)

highest_number_of_repetitions = 0
the_largest_letter_in_the_alphabet = None

for i in sorted_C:
    if C[i] > highest_number_of_repetitions:
        highest_number_of_repetitions =  C[i]
        the_largest_letter_in_the_alphabet = i


print(f"{the_largest_letter_in_the_alphabet}{highest_number_of_repetitions}")






