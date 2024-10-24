
count = 0
maxysl=0

posled = ""

def itstwo(num):
    num = int(num)
    return num % 2 ==0

with open("2523") as lines:
    line = lines.readline().strip()

    for dig in line:
        if dig.isdigit():
            posled = posled + dig
        else:
            if len(posled) !=0:
                if itstwo(posled) == False:
                    if int(posled) > maxysl:
                        maxysl = int(posled)


            posled = ""
    if len(posled) != 0:
        if itstwo(posled) == False:
            if int(posled) > maxysl:
                maxysl = int(posled)

print(maxysl)




