# def F(A,H):
#     #Старт 1
#     #Патрик 2
#     #Валера 3
#     if A <= 13 and H == 3:
#         return True
#     if A <= 13 and H!= 3:
#         return False
#     if A > 13 and H == 3:
#         return False
#
#     if H % 2 == 0: #Т.е. дальше ход Валеры
#         return F(A-2,H+1)  or  F(A // 1.5,H+1)
#     else:
#         return F(A - 2, H + 1) and F(A // 1.5, H + 1)
# for s in range(14,100):
#     if F(s,1):
#         print(s)
#         break
#21

#20:
# def F(A,H):
#     #Старт 1
#     #Патрик 2
#     #Валера 3
#     if A <= 13 and H == 4:
#         return True
#     if A <= 13 and H!= 4:
#         return False
#     if A > 13 and H == 4:
#         return False
#
#     if H % 2 == 0: #Т.е. дальше ход Валеры
#         return F(A-2,H+1)  and  F(A // 1.5,H+1)
#     else:
#         return F(A - 2, H + 1) or F(A // 1.5, H + 1)
# def Fs(A,H):
#     #Старт 1
#     #Патрик 2
#     #Валера 3
#     if A <= 13 and H == 2:
#         return True
#     if A <= 13 and H!= 2:
#         return False
#     if A > 13 and H == 2:
#         return False
#
#     if H % 2 == 0: #Т.е. дальше ход Валеры
#         return Fs(A-2,H+1)  and  Fs(A // 1.5,H+1)
#     else:
#         return Fs(A - 2, H + 1) or Fs(A // 1.5, H + 1)
# for s in range(14,100):
#     if F(s,1) and not(Fs(s,1)):
#         print(s)
#23 24

#21:
def F(A,H):
    #Старт 1
    #Патрик 2
    #Валера 3
    if A <= 13 and (H == 3 or H == 5):
        return True
    if A <= 13 and H!= 5:
        return False
    if A > 13 and H == 5:
        return False

    if H % 2 == 0: #Т.е. дальше ход Валеры
        return F(A-2,H+1)  or  F(A // 1.5,H+1)
    else:
        return F(A - 2, H + 1) and F(A // 1.5, H + 1)
def Fs(A,H):
    #Старт 1
    #Патрик 2
    #Валера 3
    if A <= 13 and H == 3:
        return True
    if A <= 13 and H!= 3:
        return False
    if A > 13 and H == 3:
        return False

    if H % 2 == 0: #Т.е. дальше ход Валеры
        return Fs(A-2,H+1)  or  Fs(A // 1.5,H+1)
    else:
        return Fs(A - 2, H + 1) and Fs(A // 1.5, H + 1)
for s in range(14,100):
    if F(s,1) and not(Fs(s,1)):
        print(s)
#25