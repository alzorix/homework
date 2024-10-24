all_dist = list()
count= 0
def itsgood(quest1:str,quest2:str,quest3:str):
    if  quest1.isdigit() and  (not (quest2.isdigit())) and  quest3.isdigit():
        return True
    else:
        return False




# with open("5391") as lines:
#     line = lines.readline().strip()
#     for l in  range(0,len(line)-2,3):
#
#         if itsgood(line[l],line[l+1],line[l+2]):
#             print(line[l],line[l+1],line[l+2])
#             count= count+1
#         else:
#             all_dist.append(count)
#             count = 0
# print(max(all_dist))
#В отличии от 5387 тут на одну больше,почему?

count = 0


T = list()
with open("5391") as lines:
    line = lines.readline().strip()
    line= "C2CB3CA3BA2AB3A"
    line= "3A15B3A67B89C1"

    l = 0
    while l <= len(line) -2 :

        if itsgood(line[l],line[l+1],line[l+2]):
            count +=1
            l = l +3
        else:
            if count > 0:

                T.append(count)
                count=0
                l = l - 1
            else:
                l = l + 1
    if count != 0:
        T.append(count)
print(max(T))

