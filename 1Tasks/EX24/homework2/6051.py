all_dist = list()
count= 0

good = [  "A",         "E",   "O"   ]
def itsgood(quest1:str,quest2:str,quest3:str):
    cot =0
    if quest1 not in good:
        cot+=1
    if quest2 not in good:
        cot+=1
    if quest3 in good:
        cot+=1
    if cot ==3:
        return True
    else:
        return False



#
# with open("6051") as lines:
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





count = 0

T = list()
with open("6051") as lines:
    line = lines.readline().strip()

    l = 0
    while l <= len(line) -3 :

        if itsgood(line[l],line[l+1],line[l+2]):
            count +=1
            l = l +3
        else:
            T.append(count)
            count=0
            l = l + 1
    if count != 0:
        T.append(count)
print(max(T))