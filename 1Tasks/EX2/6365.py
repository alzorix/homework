print("F1 = (w → z) ≡ (y → x),    F2 = (w → z) ∧ (¬x ≡ y)")
print("x y z w f1 f2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 =  (w <- z) == (w<=z)

                F2 = (w <=z)and(not(x) == y)
                if F1:
                    F1 = 1
                else: F1 = 0
                if F2:
                    F2 = 1
                else: F2 = 0

                print(x ,y ,z,w , F1,F2)

print("ответ: -")