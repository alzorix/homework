#(x → (y → z)) ∧ (y → (z ≡ ¬w))1

print("w,z,y,x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x <= (y <= z)) and (y <= (z == (not(w)))):
                    None
                else:
                    print(w,z,y,x)

