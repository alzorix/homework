print("¬w ∧ (y ∨ z → ¬x ∧ y) ")
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(w)) and ((y or z) <= ( (not(x)) and y)):


                    print(x,y,z,w)
print("ответ: wzyx ")