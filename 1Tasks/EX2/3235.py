print(''' (w → y) ∧ ((x → z) ≡ (y → x))''')
print("w z x y")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w<=y) and ( (x <=z ) == (y <= x)):
                    print(w,z,x,y)
print("ответ: wzyx ")