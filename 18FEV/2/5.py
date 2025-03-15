

data = list()
for N in range(1,10000):
    N = 9
    octN = oct(N)[2::]

    if N % 2 == 0:
        octN= octN.replace("1","2")
        octN= octN.replace("3","2")
        octN= octN.replace("5","2")
        octN= octN.replace("7","2")
    else:

        octN = "3"+octN[1:-1]+ "3"

    R = int(octN,8)
    if R <=300:
        data.append(R)
print(max(data))

#27