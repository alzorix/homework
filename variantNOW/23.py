def F(start=48,end=4,seventeen=0,twentyfive=0):
    if start == end and seventeen and twentyfive:
        return 1
    if start <= end :
        return 0

    if start == 17:
        seventeen+=1
    if start == 25:
        twentyfive+=1

    if start == 15:
        return 0

    return F(start-2,end,seventeen,twentyfive) + F(start-3,end,seventeen,twentyfive) + F(start//3,end,seventeen,twentyfive)

print(F())
#9540