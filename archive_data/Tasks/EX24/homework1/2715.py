def itstwo(num):
    return num % 2 ==0
count = 1
maxcount = 0
with open("2715") as s:
    line =  s.readline().strip()
    for l in range(len((line))-1):
        if itstwo(int(line[l])) == itstwo(int(line[l+1])):
            count+=1
        else:
            if count> maxcount:
                maxcount = count
            count=1

    if count > maxcount:
        maxcount = count
print(maxcount)