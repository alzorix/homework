
maxcountAstr = -float("inf")
maxcountA = -float("inf")

alfabet = "Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M".split(",")
rastoainie = list()
with open("4041") as file:
    line = file.readline().strip()
    count = 0
    while line !="":
        if line.count("G") <15:
            for i in alfabet:
                if line.count(i) >1:
                    rastoainie.append(abs(line.find(i)- line.rfind(i)))




        line = file.readline().strip()

print(max(rastoainie))
