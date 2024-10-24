def OTAs(num):
    F = list()
    q = 2
    while q**2 <= num:
        if num % q == 0:
            F.append(q)
            num = num//q
        else:
            q +=1
    F.append(num)

    return F
count = 1
for i in range(800_000,100_000_000):
    result = OTAs(i)
    result = max(result) + min(result)
    if str(result)[-1::] == "4":
        if count <6:
            print(i,result)
            count+=1
        else:
            break
# 800007 284
# 800013 266674
# 800019 8084
# 800035 3024
# 800039 7584