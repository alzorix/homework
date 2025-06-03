print("((x → w) ∨ y ∧ ¬z) ∧ ((y → ¬z) ∨ x ∧ ¬w). ")
print("z w y x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(      ((x<=w) or (y and (not(z)) ) ) and ((y<= (not(z))) or (x and (not(w))))           ):


                    print(z,w,y,x)
print("ответ: z,w,y,x ")