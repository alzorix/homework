'''Определите количество восьмизначных 15-ричных чисел, в записи которых
ровно два нуля и не более четырёх цифр, для записи которых используются
буквы.'''

alfabet = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E')


alfabet_S = ('1','2','3','4','5','6','7','8','9','A','B','C','D','E')

for a1 in alfabet_S:
    for a2 in alfabet:
        for a3 in alfabet:
            for a4 in alfabet:
                for a5 in alfabet:
                    for a6 in alfabet:
                        for a7 in alfabet:
                            for a8 in alfabet:
                                line = a1+a2+a3+a4+a5+a6+a7+a8
                                if line.count("0") ==2:
                                    print(line)

# #Слишком много перебора,как сделать проще? Очень долго.

# from itertools import product
# for NOLINE in product('0123456789ABCDE',repeat= 8):
#     line = "".join(NOLINE)
