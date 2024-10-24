'''(№ 6893) (Н. Сафронов) В файле 17-386.txt содержится последовательность целых неотрицательных чисел, не превышающих 10000.
 Определите количество троек элементов последовательности, в которых каждое число содержит цифру 3 в десятичной записи,
  а сумма элементов такой тройки является простым числом. В ответе запишите два числа: сначала количество найденных троек,
   затем минимальную сумму элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности. '''
lines = list()
def simpledigitl(num):
    for i in range(2,(num//2+1)):
        if num % i == 0:
            return True
    return False
print(simpledigitl(int(input())))




with open("File") as file:
    line = file.readline().strip()
    while line != "":
        lines.append(int(line))
        line = file.readline().strip()
print("list:" + f"{lines}")
F = list()
for i in range(len(lines)-2):
    if str(3) in str(lines[i]) and str(3) in str(lines[i +1 ]) and str(3) in str(lines[i + 2]) :
        good = lines[i] + lines[i+1]+ lines[i+2]
        if simpledigitl(good) != True:
            F.append(good)
print(F)
print(len(F),min(F))




