'''F = ¬(¬w ≡ y) ∨ ¬x ∨ (z ∧ w)'''
print("z,x,w,y")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (not((not(w))) == y) or (not(x)) or (z and w):
                    None
                else:
                    print(z,x,w,y)