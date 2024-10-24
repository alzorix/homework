'''w ∨ (x → y) ∧ (¬z → x)'''
#   ∨-or
print("w z y x")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if w or ((x <= y) and ((not(z)) <= x)):
                    None
                else:
                    print(w,z,y,x)