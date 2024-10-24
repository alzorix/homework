lines = list()

SUPER = -float("inf")
lines = list()
with open("17.txt") as file:
    line = file.readline().strip()
    while line != "":
        intline = int(line)
        lines.append(intline)
        if line[-3::] == "121":
            if intline > SUPER:
                SUPER = intline

        line = file.readline().strip()

def del2(num):
    if num % 2 ==0:
        return 1
    return 0
def interestingcalc(lines1,lines2,lines3):
    count = 0
    #lines1

    if len(str(lines1)) == 4:
        if del2(lines1):
            count +=1

    #lines2
    if len(str(lines2)) == 4:
        if del2(lines2):
            count +=1
    # lines3
    if len(str(lines3)) == 4:
        if del2(lines3):
            count +=1
    if count <=1:
        return True


    #if len(str(lines1)) ==3 and len(str(lines2))==3:
        #if del2(lines1) + del2(lines2) + del2(lines3) <= 1:
            #return True

    #elif len(str(lines2)) ==3 and len(str(lines3))==3:
        #if del2(lines1) + del2(lines2) + del2(lines3) <= 1:
            #return True

    #elif len(str(lines1)) ==3 and len(str(lines3))==3:
        #if del2(lines1) + del2(lines2) + del2(lines3) <= 1:
            #return True
    #return True



    return False



summs = list()

for i in range(0,len(lines)-2):
    summ = lines[i] + lines[i+ 1  ] + lines[i+ 2  ]
    if summ <= SUPER:
        if interestingcalc(abs(int(lines[i+0] )), abs(int(lines[i+1])) , abs(int(lines[i+2]))):
            summs.append(summ)
print(len(summs),max(summs))





