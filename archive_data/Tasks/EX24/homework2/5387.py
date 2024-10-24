# all_dist = list()
# count= 0
#
# with open("5387") as lines:
#     line = lines.readline().strip()
#     for l in  range(0,len(line)-1,2):
#
#         if ( line[l].isdigit() and (not line[l+1].isdigit())  )  or (  line[l+1].isdigit() and (not line[l].isdigit()  ) ):
#             print(line[l],line[l+1])
#             count= count+1
#         else:
#             all_dist.append(count)
#             count = 0
# print(max(all_dist))
# #Как проверить C3? (Первую подходящию пару)
#


count = 0


T = list()
with open("5387") as lines:
    line = lines.readline().strip()

    l = 0
    while l <= len(line) -2 :

        if (  line[l+1].isdigit() and (not line[l].isdigit()  ) ):
            count +=1
            l = l +2
        else:
            T.append(count)
            count=0
            l = l + 1
    if count != 0:
        T.append(count)
print(max(T))

# Теперь на 1 больше