'''(№ 5457) Найдите числа большие 2000000, сумма и произведение делителей которых нечётны. В ответе укажите наименьшие 6 таких чисел,
 количество делителей которых больше 30. В ответе запишите найденные числа в порядке возрастания, справа от каждого числа запишите его наибольший делитель,
  являющийся простым числом. '''




from math import sqrt






def simplegit(num):
    D = list()
    KOREN = int(sqrt(num))
    for i in range(1,KOREN +1):
        if num % i == 0 :
            D.append(i)
            if num // i != i :
                D.append(num // i)
    D.sort()
    return D





schet = 0

S = dict()
S1key = list()
for Tempint in range(2000001,2000000*10,2):
        if schet ==6:
            break

        tem2 = simplegit(Tempint)
        ltem2 = len(tem2)

        if ltem2 > 30 :

            ISK = 0


            for i in range(ltem2-1,-1,-1):

                if len(simplegit(tem2[i])) ==2:
                    ISK = tem2[i]
                    break


            if ISK != 0:
                if sum(tem2) % 2 !=0:
                    # if proiz(tem2) % 2 !=0:
                        #S1key.append(Tempint)
                        print(Tempint,ISK)

                        #S[Tempint] = ISK
                        schet +=1

S1key.sort()

for i in S1key:
    print(i,S.get(i) )
