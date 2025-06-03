print("¬(((¬w → ¬y) → ¬z) → x)")
print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    F1 = not(((not(w) <= (not(y)) ) <= (not(z))) <= x)
                    if F1:
                        F1 = 1
                    else:
                        F1 = 0

                    print(y,x,z,w,F1)

print("ответ: - ")