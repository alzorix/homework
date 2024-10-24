forSTAR = ["","1","2","3","4","5","6","7","8","9","0"]
forZNAKVOPROSA = ["1","2","3","4","5","6","7","8","9","0"]

spis = list()
for star in forSTAR:
    for znak1 in forZNAKVOPROSA:
        for znak2 in forZNAKVOPROSA:

            line = "21"+znak1+"3" +star+ "145"+ znak2+"5"
            line = int(line)
            if line % 2025 == 0:

                spis.append((line,line // 2025))
spis.sort()
for i in spis:
    d,r = i
    print(d,r)
#2123214525 1048501
#2163714525 1068501
#2173114575 1073143
