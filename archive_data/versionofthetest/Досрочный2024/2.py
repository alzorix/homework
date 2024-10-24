
















print('w,y,z,x')
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                s = (x and (not(z)) ) or ( y == z) or (not(w))
                if s == False:
                    print(w,y,z,x)
