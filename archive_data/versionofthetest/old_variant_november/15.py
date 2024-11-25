#P = [106; 218], Q = [132; 388] и R = [183;256]
def Q(x):
    return 132<=x<=388
def P(x):
    return 106<=x<=218
def R(x):
    return 183<=x<=256
a = set()
for a_start in range(1,1000):
    for a_end in range(a_start,1000):
        Flag = True
        x = 0
        while x !=300:

            if ((not(Q(x))) <= (( (P(x)) or (R(x)) ))) <= ((not(a_start <=x <= a_end)) <= (not(Q(x)))):
                None
            else:
                Flag = False
            x +=0.5
        if Flag:
            a.add(a_end - a_start + 1)
print(a)
#169