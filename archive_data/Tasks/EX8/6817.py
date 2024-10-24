'''(№ 6817) (ЕГЭ-2023) Сколько существует шестнадцатеричных трёхзначных чисел, в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом? '''
a = 0
from itertools import product,permutations
s = set()
s1 = set()
for i in product("02468ACE",repeat = 2):
    wr = "".join(i)
    s.add(wr)
#print(s)

for i in product("13579BDF",repeat = 2):
    wr = "".join(i)
    s1.add(wr)
#print(s1)

for i in product("0123456789ABCDEF",repeat = 3):
    F = "".join(i)
    if F[0] != "0":

      if F[:2] not in s1 and F[:2]  not in s and F[1:] not in s1 and F[1:]  not in s:

          if len(set(F)) == 3:
                a = a + 1

    #print(F)
print(a)

print(840)
