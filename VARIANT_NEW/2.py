for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(z or (w<=y))) or (x<=z)):
                    None
                else:
                    print(x,w,y,z)