def F(start,end,fourteen):

    if start ==8:
        return 0
    if start == 14:
        fourteen = True

    if start == end and fourteen:
        return 1
    elif start >= 18:
        return 0

    return F(start+1,end,fourteen)+F(start+2,end,fourteen)+F(start*2,end,fourteen)

print(F(3,18,False))