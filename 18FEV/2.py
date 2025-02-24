for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(x) or y) or (y==z) or not(w):
                    None
                else:
                    print(w,x,y,z)
