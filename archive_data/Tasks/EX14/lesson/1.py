a =5*216**1256 - 5*36**1146 + 4*6**1053 - 1087

def six(num):
    a = 0
    while num > 0:
        a = a + num% 6
        num = num // 6
    return a
print(six(a))



