

print("Первый вариант:")

def DEL(n,m):
    return  n% m ==0
for A in range(1000,1,-1):
    Flag = True
    for x  in range(1,999):
        if (((not(DEL(x,A)))) <=( DEL(x,28) <= (not(DEL(x,49) ))) ):
            None
        else:
            Flag = False
            break
    if Flag == True:
        print(A)
        break
print("Второй вариант:")

import time
start = time.time()


def B(x):
    return 24<=x<=90
def C(x):
    return  47<=x<=115
a = list()
for a1 in range(1,999):
    for a2 in range(a1+1,999):
        FLAG = 0
        x = -120 # Взял на всякий случай такой же  x ,как и в задании ,над котором мы долго думали. РЕШАЕТ ДОЛГО
        while x<120:
            x = x + 0.1
            if  (C(x) <= ((not(a1<= x<=a2))  and B(x)        )) <= (not(C(x))):
                None
            else:
                FLAG +=1
                break
        if FLAG ==0:
            a.append(a2-a1)
print(min(a))






finish = time.time()

# вычитаем время старта из времени окончания и получаем результат в миллисекундах
res = finish - start
res_msec = res * 1000
print('Время работы в миллисекундах: ', res_msec)