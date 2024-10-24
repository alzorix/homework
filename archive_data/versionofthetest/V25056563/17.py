
def Abs_solv(num:int):
    F = list()
    while num !=0:
        F.append(str(num% 9))
        num = num//9
    F.reverse()
    return "".join(F)






max_three = -float("inf")
all_list = list()

with open("17.txt") as fl:
    line = fl.readline().strip()

    while line !="":
        intline = int(line)

        test_ysl = Abs_solv(abs(intline))


        if test_ysl[-1] == "3":
            if intline > max_three:
                max_three = intline

        line = int(line)
        all_list.append(line)

        #print(1)
        line = fl.readline().strip()


#print(max_three)

def ysl1(chlen_troiki):
    if abs(chlen_troiki) % 2 ==0:
        if len(str(abs(chlen_troiki))) ==4:
            return True
    return False


good_sums = list()
for i in range(len(all_list)-2):
    if ysl1(all_list[i]) + ysl1(all_list[i+1]) + ysl1(all_list[i+2]) <=1:
        test = all_list[i] +all_list[i+1] +all_list[i+2]
        if test <= max_three:
            good_sums.append(test)
print(len(good_sums),max(good_sums))
# 6281 99699 - верный ответ
