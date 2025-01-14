one_shot = 3840*2160*24 # I = K * i

oneslot = 16*1024*1024*8 # Гбайт Кбайт байт бит

shots =3742
c = 0

for x in range(shots):

    if (oneslot - one_shot) >0:
        oneslot =  oneslot - one_shot
        c+=1
    else:

        #print(oneslot - one_shot)
        c = 0
        oneslot = 16*1024*1024*8
print(c)


#Где я ошибся?

