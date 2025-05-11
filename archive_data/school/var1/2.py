# ( x and (not(y))) or (x==z) or w
print("y x w z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( x and (not(y))) or (x==z) or w:
                    None
                else:
                    print(y,x,w,z)
