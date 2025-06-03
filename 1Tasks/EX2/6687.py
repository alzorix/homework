print(" (x ˄ y) ˅ (y ≡ z) ˅ w")
print("z y w x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and y) or (x == y) or w):
                    print(z,y,w,x)