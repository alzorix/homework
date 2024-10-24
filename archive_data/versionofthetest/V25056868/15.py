def P(X):
    return 15<= X<=40
def Q(X):
    return 21<=X<= 63


a = list()

for a1 in range(1,100):
    for a2 in range(a1+1,100):
        FLAG = 0
        X = -100
        while X<100:
            X = X + 0.5
            if (P(X)) <= (((Q(X)) and (not(a1<=X <=a2)) ) <= (not(P(X)))):
                None
            else:
                FLAG += 1
                break

        if FLAG ==0:
            a.append(a2-a1)


print(min(a))
#19