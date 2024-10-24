'''(№ 6788) (ЕГЭ-2023) Назовём маской числа последовательность цифр, в которой также
могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том
числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Найдите все числа, меньшие 108, соответствующие маске 1*2??76 и делящиеся без остатка
на 1923. В качестве ответа приведите все найденные числа в порядке возрастания, справа
от каждого числа выведите результат его деления на 1923'''

#7 букв - маска,а ограничение 8 => star 0,1,2 букв
alfabet =set()
from itertools import product
for a in product("0123456789",repeat =1):
    s = "".join(a)
    alfabet.add(s)
for a in product("0123456789",repeat =2):
    s = "".join(a)
    alfabet.add(s)

alfabet.add("")

ansewers = list()
for quest in range(10):
    for quest2 in range(10):
     for star in alfabet:

        line = "1"+star+"2"+str(quest) + str(quest2)+ "76"
        line = int(line)
        if line <= 10**8:
         #print(line)
         if line %1923 ==0:
            ansewers.append((line,line//1923))
        else:
            print(len(star))
ansewers.sort(key = lambda x:x[0])
for x in ansewers:
    s,r = x
    print(s,r)
#print(ansewers)