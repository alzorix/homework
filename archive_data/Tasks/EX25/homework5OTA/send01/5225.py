'''(№ 5225) Пусть N(k) = 9 500 000 + k, где k – натуральное число. Найдите пять наименьших значений k,
 при которых N(k) нельзя представить в виде произведения трёх натуральных чисел, больших 1.
  В ответе запишите найденные значения k в порядке убывания, справа от каждого значения запишите наибольший делитель N(k), не равный самому числу. '''


from math import sqrt
def OTAs(num):
    F = list()
    num = int(num)
    q = 2
    while q**2 <= num:


        if num % q == 0:
            F.append(q)
            num = num//q
        else:
            q +=1
    F.append(num)

    return F

s = 0
x = 0
while s !=5:
    a = 9500000 + x
    if len(OTAs(a)) !=3:
        print(x,OTAs(a),a)
        s+=1
    x +=1

# Что тут не так? (Функция сортировка будет написана позже)