'''(№ 5335) (ЕГЭ-2022) Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
в записи которых ровно одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6. '''

from itertools import product,permutations
s = set()
for i in product("01234567",repeat = 5):
    wr = "".join(i)

    if wr[0] != "0":
        if wr.count("6") == 1:
            six = wr.find("6")

            if six == 0:
                if wr[six + 1] not in "1357":
                        s.add(wr)

            elif six == 4:
                if wr[six - 1] not in "1357":
                        s.add(wr)
            else:
                if wr[six - 1] not in "1357":
                    if wr[six + 1] not in "1357":
                        s.add(wr)

print(len(s))