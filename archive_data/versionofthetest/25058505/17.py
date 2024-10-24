integers = list()

with open("17_17873.txt") as file:
    line = file.readline().strip()
    while line !="":
        integers.append(int(line))
        line= file.readline().strip()

min_ = min(integers)

ansewers = list()
for i in range(len(integers)-1):
    a = integers[i] % 16
    b = integers[i+1] % 16
    if a == min_ or b == min_:
        ansewers.append(integers[i]+integers[i+1])
print(len(ansewers),max(ansewers))
#1099 177727