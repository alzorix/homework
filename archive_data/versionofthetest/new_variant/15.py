#F = (x - 3y <A) or (y>400) or (x>56):


for A in range(1,10000):
    F = True
    x = 1
    while x<=500:
        y = 1
        while y <=500:
            if (x - 3*y <A) or (y>400) or (x>56):
                None
            else:
                print(x,y,)
                F = False
                break
            y+=1
        if not(F):
            print(x, y)
            break
        x+=1
    if F:
        print(A)
        exit()
#957