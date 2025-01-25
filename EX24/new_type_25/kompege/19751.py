'''Текстовый файл состоит из цифр от 1 до 9, знаков операций «+», «–» и «*» (сложение, вычитание и умножение) и
 заглавных латинских букв A, B, C, D. Назовём правильной суммой строку, содержащую последовательность из одного или более десятичных чисел,
  в которой между соседними числами стоит ровно один знак «+» и нет других знаков.
Примеры правильных сумм: «23», «115+6», «1980+12+12351».
Назовём результатом правильной суммы число, которое получится при выполнении записанных в соответствующей строке сложений.
 Например, результат правильной суммы «2+3» – число 5
Найдите в данной строке правильную сумму, расположенную непосредственно после буквы A и имеющую наибольший результат.
В ответе запишите результат найденной суммы. Гарантируется, что ответ не превышает 2·109.'''


with open("24_19751.txt") as f:
    line = f.readline().strip()



line = line.replace("B","#")
line = line.replace("C","#")
line = line.replace("D","#")
line = line.replace("-","#")
line = line.replace("*","#")
line = line.replace("++","#")

src_lines = line.split("#")

maxx = 0

for id in range(1,len(src_lines)):
    local_line  = src_lines[id]

    if "A" in local_line: #+01+A+01+A+01+

        c = local_line.count("A")
        if c ==1 and local_line[-1] != "A":
            t = local_line.split("A")


            try:
                maxx = max(maxx,eval(t[1].rstrip("+")))
            except SyntaxError:
                None
        elif c > 1:

            split_A = local_line.split("A")
            for index in range(1,len(split_A)):
                x = split_A[index].rstrip("+")

                #print(x)
                try:
                    if eval(x) == 891345854:
                        print(local_line)
                    maxx = max(maxx, eval(x))

                except SyntaxError:
                    None

print(maxx)
#67622777






