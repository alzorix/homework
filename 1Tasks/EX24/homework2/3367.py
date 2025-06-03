
count = 1
all_distances = list()
with open("3349") as s:

    line = s.readline().strip()

    for l in range(len(line)-1):

        if ord(line[l]) < ord(line[l+1]):
            count+=1
        else:
            all_distances.append(count)
            count = 1
    all_distances.append(count)





print(max(all_distances))



#2457_1_