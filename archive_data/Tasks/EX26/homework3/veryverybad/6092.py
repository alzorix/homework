
mm = -float("inf")


with open("../../homework1/files/26-101.txt") as file:
    temp = file.readline().strip().split(" ")
    line = file.readline().strip()
    N = temp[0] # кол-во конт
    ysl = temp[1] #условие помещение
    ysl = int(ysl)

    list_cell = list()
    all_cont = list()
    while line != "":
        all_cont.append(int(line))

        line = file.readline().strip()

    all_cont.sort(reverse=True)
    special_list = list()
    while True:
        if all_cont[0] == 0:
            break
        start = [all_cont[0]]
        all_cont.pop(0)
        all_cont.append(0)
        i = 0
        while i < len(all_cont):
            if all_cont[i] == 0:
                break
            if start[-1] - all_cont[i] >= ysl:
                start.append(all_cont[i])
                all_cont.pop(i)
                all_cont.append(0)
                i  = i -1


            i+=1
        special_list.append(start)
print(len(special_list),max([len(x) for x in special_list]))




