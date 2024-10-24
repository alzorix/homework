print( "¬x ∧ ((z → y) → w)")
print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    F = not(x) and ((z <= y) <=w)
                    if F:
                        F = 1
                    else:
                        F = 0

                    print(y,x,z,w,F)

print("ответ: - ")