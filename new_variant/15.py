#F = (x - 3y <A) or (y>400) or (x>56):


for A in range(1,10000):
    F = True
    x = -300

    while x<=300:
        y = -300
        while y <=300:
            if (x - 3*y <A) or (y>400) or (x>56):
                None
            else:
                F = False
                break
            y+=0.5
        if not(F):
            break
        x+=0.5
    if F:
        print(A)
        exit()
#957