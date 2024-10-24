alfabet = [str(c) for c in range(100)]
alfabet.append("")


for s in range(10):

        i = "0"
        s = str(s)
        alfabet.append( i + s)

ans = list()
for quest in alfabet:

    for  star in range(10):
        for star_ in range(10):


            lube = "3"+ str(star) + "12" + str(star_) + "14"+ quest + "5"

            lube = int(lube)
            if lube % 1917 ==0:
                ans.append((lube,lube //1917))

ans.sort()
for i in ans:
    t,d = i
    print(t,d)
    #3212614035 1675855 НЕТ