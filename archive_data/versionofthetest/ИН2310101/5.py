
a = set()
for N in range(100000,99999999):
    C = bin(N)[2::]



    binN =  bin(N%3)[2::].zfill(2)
    C = C + binN

        #print(1)

    binN  = bin(int(C,2) % 5)[2::].zfill(3)
    C = C + binN


    R = int(C,2)
    if 1111111110 <= R <=1444444417:
        a.add(R)

    #     else:
    #         print("error 2")
    #
    #


print(len(a))

#В чем проблема?
