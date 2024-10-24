# F = list()
# with open("24.txt") as file:
#     line = file.readline().strip()
#     good_line = ""
#     red_flag_count = 0
#     for i in line:
#         try:
#             a = eval(good_line + i)
#             good_line = good_line + i
#             if eval(good_line) == 0:
#                 F.append(len(good_line))
#
#         except:
#             if i !="0":
#                 red_flag_count +=1
#             if red_flag_count >4:
#                 red_flag_count = 0
#                 good_line = ""
# print(max(F))
# #10


with open("24.txt") as file:

    m= 0

    line = file.readline().strip()
    while "**" in line:
        line = line.replace("**","* *")
    while "++" in line:
        line = line.replace("++","+ +")
    while "*0" in line:
        line = line.replace("*0","* 0")
    while "+0" in line:
        line = line.replace("+0","+ 0")
    while "+*" in line:
        line = line.replace("+*","+ *")
    while "*+" in line:
        line = line.replace("*+","* +")

    print(line.split(" "))