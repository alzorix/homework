def F(A,H):
    # 1 - start
    # 2 - Ход Пети
    # 3 - Ход Вани

    if A >= 67 and H ==3:
        return True
    if A >= 67:
        return False
    if H >=3:
        return False

    if H % 2 ==0: #Был ход Пети,теперь ход Вани
        return F(A+1,H+1) or F(A+4,H+1) or F(A*3,H+1)
    else:
        return F(A + 1, H + 1) and F(A + 4, H + 1) and F(A * 3, H + 1)

for S in range(1,67):
    if F(S,1):
        print(S)
#22
