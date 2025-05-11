'''Определите количество девятеричных пятизначных чисел,
 в записи которых ровно одна цифра 0,
 при этом никакая нечётная цифра не стоит рядом с цифрой 0.'''

alfabet = ['0','1','2','3','4','5','6','7','8']
c = 0
for a1 in alfabet:
    for a2 in alfabet:
        for a3 in alfabet:
            for a4 in alfabet:
                for a5 in alfabet:
                    s = a1+a2+a3+a4+a5
                    if s[0] != "0":
                        if s.count("0") ==1:
                            x = s.find("0")
                            if int(s[x-1]) % 2 == 0:
                                try:
                                    if int(s[x+1]) % 2 == 0:
                                        c +=1
                                except IndexError:
                                    c+=1
print(c)