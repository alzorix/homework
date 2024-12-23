
def P(n):
    return 10<=n<=150
def Q(n):
    return 160 <= n <= 250
def R(n):
    return 240 <= n<= 300



tr = list()
for a1 in range(-100,301):
    for a2 in range(a1, a1+ 301):
        x = -300
        FLAG = True
        while x <=300:
            if ( (Q(x)) <= (P(x)) ) or (  (not(a1<=x<=a2) )<= (R(x)) ):
                None
            else:
                FLAG = False
                break
            x +=0.5
        tr.append(a2-a1)
print(min(tr))
