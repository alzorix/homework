'''(№ 5251) (М. Шагитов) В файле 17-328.txt содержится последовательность целых чисел. Элементы последовательности – четырёхзначные натуральные числа.
 Найдите все тройки элементов последовательности, для которых восьмеричная запись суммы любой пары чисел тройки содержит только чётные цифры,
  а сумма всех чисел тройки меньше, чем сумма цифр всех чисел в файле, делящихся на 22.
В ответе запишите количество найденных троек, затем минимальную из сумм элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''


def chetnechet(num):
    chet = True
    num = str(num)
    for i in range(len(num) ):
        if int(num[i])  % 2 !=0:
            chet = False
    return chet

def calc(num:str):
    F = list()
    for i in range(len(num)):
        F.append(int(num[i]))
    return sum(F)


al = list()

last_digit_of_all_numbers_in_the_file_divisible_by_22 = 0
with open("File") as file:
    line = file.readline().strip()

    while line != "":
        line = int(line)
        if line %22 == 0:
            last_digit_of_all_numbers_in_the_file_divisible_by_22 = last_digit_of_all_numbers_in_the_file_divisible_by_22 + calc(str(line))


        al.append(line)

        line = file.readline().strip()

groups = list()
for i in range(len(al)-2):
    sum1 = chetnechet(oct(al[i] + al[i+1]  )[2::])
    sum2 = chetnechet(oct(al[i+2] + al[i+1]  )[2::])
    sum3 = chetnechet(oct(al[i+2] + al[i]  )[2::])

    if sum3  and sum2  and sum1:

        if sum(al[i:i +3]) < last_digit_of_all_numbers_in_the_file_divisible_by_22:
            print(oct(al[i] + al[i + 1])[2::], oct(al[i + 2] + al[i + 1])[2::], oct(al[i + 2] + al[i])[2::])
            #print(sum(al[i:i +2]),al[i:i +2])
            groups.append(sum(al[i:i +3]))

print(len(groups),min(groups),groups)