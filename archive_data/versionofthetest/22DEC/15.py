
def P(n):
    return 10<=n<=150#+
def Q(n):
    return 160 <= n <= 250#+
def R(n):
    return 240 <= n<= 300#+



tr = list()
for a1 in range(-400,401):  #Значения были изменены,для того,чтобы убедиться в правильности ответа
    for a2 in range(a1, a1+ 401): #Значения были изменены,для того,чтобы убедиться в правильности ответа
        x = -300
        FLAG = True
        while x <=300:
            if ( (Q(x)) <= (P(x)) ) or (  (not(a1<=x<=a2) )<= (R(x)) ): #+
                None
            else:
                FLAG = False
                break
            x +=0.5
        if FLAG: # Не было условия как не странно
            tr.append(abs(a2-a1)) # длина не может быть отрицательной
print(min(tr))
#80