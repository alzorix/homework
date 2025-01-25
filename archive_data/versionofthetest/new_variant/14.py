alfabet  = dict()
for x in range(10):
    alfabet[str(x)] = x
for x in range(15):
    alfabet[chr(65+x)] = x+10
#print(alfabet)

for x in alfabet.keys():
    int1 = int("11353"+x+"12",25)
    int2 = int("135"+x+"21",25)
    s = int1+int2
    if s % 24 ==0:
        print(x,s//24)
#M 266249847