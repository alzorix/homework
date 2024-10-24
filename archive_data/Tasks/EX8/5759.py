'''(№ 5759) *(Д. Статный) Григорий придумывает 16-буквенные слова, состоящие из букв слова АНТИУТОПИЯ. Сколько слов,
содержащих комбинацию АНТИУТОПИЯ, может составить Григорий, если справа от этой комбинации находится равное количество гласных и согласных,
а слева – не больше 2-х согласных? Буквы в словах могут повторяться любое количество раз или же не встречаться вовсе. '''

from  itertools import product


def right(wrlen):
    a = 0
    for i in product('АНУТОПИЯ', repeat=wrlen):
        i = "".join(i)
        if i.count("А") + i.count("И") +  i.count("У") + i.count("О")+ i.count("Я") == i.count("Н") + i.count("Т") +  i.count("П"):
             a += 1
    return a
def left(wrlen):
    a = 0
    for i in product('АНУТОПИЯ', repeat=wrlen):
        i = "".join(i)
        if i.count("Н") + i.count("Т") + i.count("П") <= 2:
            a += 1
    return a







print(right(6) + right(4) * left(2) + right(2) * left(4) + left(6) ==414400 )

