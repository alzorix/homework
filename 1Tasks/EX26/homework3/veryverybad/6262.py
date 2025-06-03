price_list =list()
balance = 100_000

with open("../../homework1/files/26-109.txt") as file:
    N = file.readline().strip()#колво-товаров
    line = file.readline().strip()
    while line!= "":
        price_list.append(int(line))
        line = file.readline().strip()

    file.close()




def sixcalc(srez):
    lens = len(srez)
    skidka = lens//6
    total_sum = 0
    for i in range(lens-skidka):
        total_sum = total_sum+srez[i]
    for i in range(skidka):
        total_sum = total_sum + srez[lens-1-i]//2

    return total_sum






price_list.sort()

s = list()

for i in range(len(price_list)):
    a = sixcalc(price_list[0:i+1])

    if a  <= balance:
        s.append((i+1,balance-a) )
print(max(s))




#Насколько я понял нужно,чтобы только оптимальные товары должны быть со скидкой,а не каждый шестой. Как это реализовать я не знаю.