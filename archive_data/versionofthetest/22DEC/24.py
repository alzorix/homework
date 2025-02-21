''' В волшебном королевстве, где звезды искрятся на ночном небе, жил-был Числовой Заклинатель.
 Он умел создавать удивительные заклинания из чисел и знаков, используя только цифры 0, 2, 3, 4, 5
  и знаки операций «+» (сложение) и «*» (умножение). Эти числа и знаки были ключами к его магии!'''

with open("24.txt") as file:
    line = file.readline().strip()
    file.close()


s = line.replace("+","*")
s = s.replace("3","2")
s = s.replace("4","2")
s = s.replace("5","2")
gs = s.split("*")

ind = 0
c = 0

for x in gs:
    if x != "" and (x =="0" or x[0] !="0"):
        ind +=len(x) +1
        c = max(c,ind-1)
    elif x !="" and (x[0] == "0" ):
        c = max(c,ind+1)
        r = x.find("2")
        if r > -1:
            ind = len(x[r::])+1
            c = max(c,ind-1)
        else:
            ind = 2
            c = max(c,ind-1)

    else:
        ind =0

print(c)


