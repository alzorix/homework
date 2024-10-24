print("y,x,w,z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                 F = (not(x<=w)) or (y<=z) or (not(y))
                 if F == 0:

                    print(y,x,w,z)

