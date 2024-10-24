print('''¬(x ≡ y → z)''')
print("x y z F")
for x in range(2):
    for y in range(2):
        for z in range(2):
                F =  not(x == (y <= z))
                if F:
                    F = 1
                else:
                    F = 0


                print(x,y,z,F)
print("ответ: yxz ")