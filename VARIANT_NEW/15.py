def delF(n,m):
    return n%m==0
def B(c):
    return 50<=c<=80

for A in range(1,100000):
    x = 0.0
    c =1
    while x<= 500.0:
        if ((B(x))<= (not(delF(x,7)))) or ((x + A) >=90):
            None
        else:
            c=0
        x += 0.5
    if c ==1:
        print(A)
        exit()

