# count = 0
# fist = True
# start_line = None
#
# T = list()
# with open("5041") as lines:
#     line = lines.readline().strip()
#
#     for l in range(2,len(line)-2,3):
#         if line[l+2] == "Y" and (line[l] ==  "X" or line[l] ==  "Z"):
#
#             if fist:
#                 start_line = l
#                 fist = False
#                 count += 1
#
#             else:
#
#                 count +=1
#         else:
#             fist = True
#
#             T.append(count)
#             count=0
#     T.append(count)
# print(max(T))
#
#
#
# count = 0
# fist = True
#
# T = list()
# with open("5041") as lines:
#     line = lines.readline().strip()
#
#     l = 2
#     while l <= len(line) -2 :
#
#         if line[l+2] == "Y" and (line[l] ==  "X" or line[l] ==  "Z"):
#             count +=1
#             l = l +3
#         else:
#             T.append(count)
#             count=0
#             l = l + 1
#     T.append(count)
# print(max(T))


#XZYYXXY
with open("5041") as lines:
    line = lines.readline().strip()
    spisok = [0]*(len(line)+3)
    for i in range(len(line)-2):
        if line[i] + line [i+2] in ("XY","ZY"):
            spisok[i+3] = max(spisok[i+3],spisok[i] +3)
print(max(spisok)//3)