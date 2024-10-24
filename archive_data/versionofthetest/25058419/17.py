integers = list()

with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":
        integers.append(int(line))
        line= file.readline().strip()

avarage = min(integers)

ansewers = list()
for i in range(len(integers)-1):
    a = integers[i] % 77
    b = integers[i+1] % 77
    if a+b == avarage:
        ansewers.append(integers[i]+integers[i+1])
print(len(ansewers),max(ansewers))
#35 186613