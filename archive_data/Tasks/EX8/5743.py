'''(№ 5743) (М. Ишимов) Определите количество чисел, девятеричная запись которых содержит ровно 6 цифр, из которых не более двух нечётных,
 а сумма всех цифр этой записи кратна 6, но не кратна 4. '''

from itertools import  product
chislo = 0
for i in product("012345678",repeat = 6):
    i ="".join(i)
    if i[0] != "0":
        NECHET = i.count("1") + i.count("3") + i.count("5") + i.count("7")
        if NECHET < 3:
            a = 0

            for temp in range(6):

                a = a + int(i[temp])
            if a % 6 == 0 and a % 4 != 0:
                    chislo += 1


print( 23733 == chislo)
print( chislo)
