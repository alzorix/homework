
maxcountAstr = -float("inf")
maxcountA = -float("inf")



with open("3785") as file:
    line = file.readline().strip()
    count = 0
    while line !="":

        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                count+=1
            else:
                if count > maxcountA:
                    maxcountAstr = line
                    maxcountA = count
                count = 0


        if count > maxcountA:
            maxcountAstr = line
            maxcountA = count

        line = file.readline().strip()


test = dict()
for i in maxcountAstr:
    if i in test:
        test[i] +=1
    else:
        test[i] =1


print(test)
a = (sorted(test))

a.reverse()


max_test = min(test.values())
for i in a:
    if test.get(i) == max_test:
        need_str = i
        break

final_count = 0

with open("3785") as file:
    line = file.readline().strip()
    while line !="":
        for i in line:
            if need_str == i:
                final_count +=1


        line = file.readline().strip()

print(need_str,final_count)

