def P(x):
    return  15<= x <= 142
def Q(x):
    return  38<= x <= 167
AAA = list()
for A1 in range(-170,170):
    for A2 in range(A1+1,A1+170):
        Its_good = True
        x:float = -170.0
        while x <=170.0:
            if (not( (Q(x)) <= (( (not((A1<=x<=A2))) and (P(x))    )  <= (not(Q(x)))                    )) ):

                Its_good = False

            x+=0.5
        if Its_good:

            AAA.append(A2-A1)
print(min(AAA))
#104