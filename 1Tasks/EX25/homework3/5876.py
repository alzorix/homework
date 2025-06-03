'''(№ 5876) (Е. Джобс) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.

Например, маске 123*4?5 соответствуют числа 123405 и 12300405.

 Среди натуральных чисел, меньших, чем 1013, найдите числа, соответствующие маске 32*54?123 и делящиеся на 519, в которых
 1) чётное количество цифр, среди которых нет нулей;
 2) сумма цифр первой половины числа равна сумме цифр второй половины числа.

  Запишите в ответе найденные числа в порядке возрастания, справа от каждого числа укажите частное от его деления на 519.  '''


from itertools import product
a2 = list()
a2.append("")
for i in product("246813579",repeat =1):
    a2.append("".join(i))

for i in product("246813579",repeat =2):
    a2.append("".join(i))

for i in product("246813579",repeat =3):
    a2.append("".join(i))

for i in product("246813579",repeat =4):
    a2.append("".join(i))

for i in product("246813579",repeat =5):
    a2.append("".join(i))

for i in product("246813579",repeat =6):
    a2.append("".join(i))

for i in product("246813579",repeat =7):
    a2.append("".join(i))


def ysl(N):
    F1= 0
    F2 = 0
    N = str(N)
    for i in range(0,int(len(N)/2)):
        F1 = F1 + int(N[i])
    for i in range(int(len(N)/2),len(N)):
        F2 = F2 + int(N[i])
    return F2 ==F1


D = list()
for quest in range(1,10):
    for star in a2:
        T = int(f"32{star}54{quest}123")
        if len(str(T)) < len(str(10**13)):
            if len(str(T))%2==0:
                if T % 519 == 0:
                    if ysl(T):

                        D.append(T)
D.sort()
for i in D:
    print(i,i//519)

















