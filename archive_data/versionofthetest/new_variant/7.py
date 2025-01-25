one_shot = 3840*2160*24 # I = K * i

oneslot = 16*1024*1024*1024*8 # Гбайт Мбайт Кбайт байт бит

shots =3742
c = 0

for x in range(shots):

    if (oneslot - one_shot) >=0:
        oneslot =  oneslot - one_shot
        c+=1
    else:

        #print(oneslot - one_shot)
        c = 1
        oneslot = 16*1024*1024*1024*8 - one_shot

print(c)
#292

#Где я ошибся?

