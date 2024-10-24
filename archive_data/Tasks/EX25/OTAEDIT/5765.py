''' 	(№ 5765) *(Д. Статный) Среди натуральных чисел, принадлежащих промежутку [35 000 000; 100 000 000],
 найдите все числа, имеющие ровно 3 делителя, отличных от 1 и самого числа. В ответ запишите найденные числа
 в порядке возрастания, справа от каждого числа запишите его максимальный делитель, отличный от самого числа. '''


def OTA(num):
    F = list()
    T = -1
    Ft = list()
    q = 2
    while q ** 2 <= num:
        if num % q == 0:
            num = num // q
            if q not in F:


                F.append(q)
                T += 1
                Ft.append(1)
                if T == 1:
                    return F, Ft
            else:
                Ft[T] += 1
                if Ft[T] > 4:
                    return F, Ft


        else:
            if T >=1:
                return F, Ft

            q += 1
    if num in F:
        Ft[T] += 1
        if Ft[T] > 4:
            return F, Ft

    else:


        Ft.append(1)
        F.append(num)
        return F, Ft

    return F, Ft

res = list()
for i in range(35000000, 100000000):


    S,r = OTA(i)

    lenS= len(S)
    lenr = len(r)


    if lenS ==1:
        if lenr ==1:
            if r[0] ==4:
                print(S,r)

                #print(i,S[0]**3)

# res.sort()
#
# for i in range(len(res)):
#     r,s = res[i]
#     print(r,s)
