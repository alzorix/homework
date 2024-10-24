
mincountAstr = float("inf")
mincountA = float("inf")



with open("3781") as file:
    line = file.readline().strip()
    while line !="":
        if line.count("A") < mincountA:
            mincountA = line.count("A")
            mincountAstr = line
        line = file.readline().strip()


test = dict()
for i in mincountAstr:
    if i in test:
        test[i] +=1
    else:
        test[i] =1



a = sorted(test)

a.reverse()


max_test = max(test.values())
for i in a:
    if test.get(i) == max_test:
        need_str = i
        break

final_count = 0

with open("3781") as file:
    line = file.readline().strip()
    while line !="":

        final_count += line.count(need_str)


        line = file.readline().strip()

print(need_str,final_count)