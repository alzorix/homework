'''(№ 7573) (ЕГЭ-2024) Текстовый файл 24-299.txt состоит не более чем из 106 символов и содержит только десятичные цифры,
 а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности,
  являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака), значение которого равно нулю.
  В этом выражении никакие два знака арифметических операций не стоят рядом, порядок действий определяется по правилам математики.
   В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество символов в найденном выражении. '''



with open("7573") as file:
    line = file.readline().strip()

line = line.replace("++","!")
line = line.replace("+*","!")
line = line.replace("*+","!")
line = line.replace("**","!")

maxx_true_digital = 0

for i in line.split("!"):
    print(i)
    if len(i) > maxx_true_digital:
        for sx in range(len(i)-1):
            if i[sx] != "+" and  i[sx] != "*" and not (i[sx] == "0" and i[sx + 1].isdigit()):
                local_t = i[sx]
                for td in range(sx + 1 , len(i)):
                    local_t += i[td]
                    if local_t[-1] != "+" and local_t[-1] != "*" and eval(local_t) == 0:
                        maxx_true_digital = max(maxx_true_digital,len(local_t))
print(maxx_true_digital)