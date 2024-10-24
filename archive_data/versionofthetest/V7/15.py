from math import  sqrt

def NOD(n,m,k):



    if n > m:
        m,n=n,m
    simplelist = list()

    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            if m % i ==0:
                simplelist.append(i)
            if m % (n//i)==0:
                simplelist.append(n//i)
    return  max(simplelist)==k






goods = 0
for A in range(1,1001):
    REDFLAG = True
    for x in range(1,999):
        if NOD(     A,420,2       ) or (not(NOD(  A,x,12        ))) <= (not (NOD(   110,x,11     ))):
            None
        else:
            REDFLAG = False

    if REDFLAG == True:
        goods +=1
print(goods)