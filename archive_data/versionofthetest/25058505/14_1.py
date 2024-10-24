#98897x21 + 2x923

alfabet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I"]
alfabet.reverse()
for x in alfabet:
    a1= int("98897"+x+"21" ,19)

    a2= int("2"+x+"923",19)
    s =a1+a2
    if s %18 ==0:
        print(s//18)
        exit()