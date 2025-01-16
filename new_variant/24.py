#Никогда данный тип не решал. Возможно что-то понял не так

# with open("24.txt") as file:
#     line = file.readline().strip()
#     c = "FSRQ"
#     print(line.count(c))

with open("24.txt") as file:
    line = file.readline().strip()
    file.close()




#7494 7494 749474947494749474947494749474947494749474947494749474947494749474947494749474947494749474947494 !!!!!!!!!!!!


# метод двух ук











# ans = list()
# c = -float("inf")
#
#
#
# def kostil(line1):
#     current_fist_FSRO = -1
#     if len(line1) <4:
#         return 1
#
#     for current_index in range(len(line1) - 3):
#         will = line1[current_index] + line1[current_index + 1] + line1[current_index + 2] + line1[current_index + 3]
#         #print(will)
#         if will == "FSRQ":
#             #print(1)
#             if current_fist_FSRO == -1:
#                 current_fist_FSRO = current_index
#
#             else:
#                 dlina = current_fist_FSRO - current_index + 3
#                 temp = line1[current_fist_FSRO: current_index + 4]
#                 if temp.count("FSRQ") == 80:
#                     ans.append(dlina)
#                     line1 =  line1[current_fist_FSRO+1::]
#                     s = kostil(line1)
#                     if s == 1:
#                         break
# kostil(line)
# print(min(ans))



#Потратил 36 минут,получилось это чудо юдо.

ans = list()
while len(line) >=4:
        k = True
        current_fist_FSRO = -1
        if len(line) < 80:
            break

        for current_index in range(len(line) - 3):
            will = line[current_index] + line[current_index + 1] + line[current_index + 2] + line[current_index + 3]
            # print(will)
            if will == "FSRQ":
                # print(1)
                if current_fist_FSRO == -1:
                    current_fist_FSRO = current_index

                else:
                    k = False
                    dlina = current_fist_FSRO - current_index + 3
                    temp = line[current_fist_FSRO: current_index + 4]
                    if temp.count("FSRQ") == 80:
                        ans.append(dlina)
                        line = line[current_fist_FSRO + 1::]
        if current_fist_FSRO == -1:
            break
        if k:
            break

print(min(ans))

#Это всё надо переделать,вообще неудачное решение,потрачено сумарно 45 минут