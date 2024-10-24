print(" w ∧ ((z ∨ y) ≡ (z ∧ x))")
print("x z y w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    F = w and ( ( z or y) == ( z and x))
                    if F:
                        F = 1
                    else:
                        F = 0

                    if F:

                     print(x,z,y,w,F)
print("ответ: xywz ")