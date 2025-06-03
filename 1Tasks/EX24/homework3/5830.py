

str_current = None
str_max = 0

count = 1
with open("5830") as s :
    line = s.readline().strip()
    for i in range(len(line)-1):

        if line[i] != line[i+1]:
            count+=1
        else:
            if count != 0:
                if count>= str_max:
                    str_max = count
                    str_current = line[i-count+1:i+1]
            count = 0




test = dict()
for i in str_current:
    if i in test:
        test[i] +=1
    else:
        test[i] =1

a = (sorted(test))


print( max(test.values()))






