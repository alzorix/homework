'''(№ 6601) (Е. Джобс) В файле 17-376.txt содержится последовательность натуральных чисел, не превышающих 10000.
 Определите количество пар элементов последовательности, в которых только одно число кратно 7,
  а сумма элементов пары кратна максимальному элементу последовательности, оканчивающемуся на 0F в шестнадцатеричной системе счисления.
   В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
    В данной задаче под парой подразумевается два идущих подряд элемента последовательности.'''
spisok = list()
the_maximum_element_of_the_sequence_ending_with_0F_in_hexadecimal_notation = -float("inf")

with open("File") as file:
    line = file.readline().strip()
    while line!= "":
        line = int(line)

        if line >the_maximum_element_of_the_sequence_ending_with_0F_in_hexadecimal_notation and hex(line)[2::][-2::] == "0f" :
            the_maximum_element_of_the_sequence_ending_with_0F_in_hexadecimal_notation = line










        spisok.append(int(line))
        line = file.readline().strip()





kolvo = list()

for m in range( len(spisok) -1):
    if (spisok[m] % 7 == 0 and spisok[m  +1 ] % 7 != 0) or (spisok[m] % 7 != 0 and spisok[m  +1 ] % 7 == 0) :

        if the_maximum_element_of_the_sequence_ending_with_0F_in_hexadecimal_notation % (spisok[m] + spisok[m+1])  ==0 or (spisok[m] + spisok[m+1]) % the_maximum_element_of_the_sequence_ending_with_0F_in_hexadecimal_notation  ==0:
            kolvo.append(spisok[m] + spisok[m+1])
print(len(kolvo),max(kolvo))
