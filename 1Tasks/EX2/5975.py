print(" (z → w) ∧ y ∧ ¬x")

print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    F = (z <= w) and y and (not(x))
                    if F:
                        F = 1
                    else:
                        F = 0

                    print(x,y,z,w,F)
print("ответ: zwyx ")