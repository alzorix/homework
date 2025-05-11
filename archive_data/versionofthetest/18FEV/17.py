database = list()
summa_chetirex = 0
with open("17.txt") as f:
    line = f.readline().strip()
    while line != "":
        line = int(line)
        if len(str(abs(line))) ==4:
            summa_chetirex +=line



        database.append(line)
        line = f.readline().strip()
    f.close()



def trexznach(digital):

    if  len(str(abs(digital))) == 3:
        return True
    return False

def ysl2(s1,s2,s3):
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)

    proiz = s1*s2*s3
    return proiz > summa_chetirex

ans = list()
for id in range(0,len(database)-2):
    s1 = database[id]
    s2 = database[id + 1]
    s3 = database[id + 2]
    if trexznach(s1) + trexznach(s2) + trexznach(s3) ==2:
        #print( trexznach(s1) , trexznach(s2) , trexznach(s3))
        if ysl2(s1,s2,s3):
            ans.append(s1*s2*s3)

print(len(ans),abs(min(ans)))

