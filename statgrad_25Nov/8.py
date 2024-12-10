'''Определите количество восьмизначных 15-ричных чисел, в записи которых
ровно два нуля и не более четырёх цифр, для записи которых используются
буквы.1'''

from  itertools import product


kolvo:int = 0

for i in product("01A",repeat =8 ):
    s = "".join(i)
    if s[0] != "0":
        if s.count("0") == 2 and s.count("A") <=4:
            kolvo+=5**s.count("A")*9**s.count("1")
print(kolvo)