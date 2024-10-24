'''((x → y) ∧ (z ≡ ¬w)) → (u ≡ (x ∨ z))'''
print("u z y x w")
for x in range(0,2):
    for u in range(0, 2):
        for w in range(0, 2):
            for y in range(0, 2):
                for z in range(0, 2):
                    if (not(((x <= y) and (z == ((not(w))))) <= (u == (x or z)))):

                        print(u, z, y,x, w)