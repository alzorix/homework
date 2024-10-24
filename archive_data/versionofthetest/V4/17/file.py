
the_min = float("inf")
spisok = list()
with open("17var04.txt") as file:
    line = file.readline().strip()

    while line!= "":

        if line[-3::] =="700":
            #print(line)
            if int(line) < the_min:
                the_min = int(line)








        spisok.append(int(line))
        line = file.readline().strip()


kolvo = list()
print(the_min)
for m in range( len(spisok) -2):

    if sum(spisok[m:m+3]) >= the_min:
        if not(len( str(abs(spisok[m]))) == 5 and len(    str(abs(spisok[m+1]))) == 5 and len(  str(abs(spisok[m+2]))) == 5):
            kolvo.append(sum(spisok[m:m+3]))




print(len(kolvo),min(kolvo))