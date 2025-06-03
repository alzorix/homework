fist_A = True
A = None
B = None

fist_B = True
count = 0
with open("4917") as s:

    line = s.readline().strip()

    for l in range(len(line)):

        if line[l] == "A":

                A = l

        if line[l] == "B":


            if A != None:
                B = l
                if (abs(A -B) +1) >=20:
                    count+=1
            A = None
#Неправильный ответ
print(count)


