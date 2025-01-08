#F = not((not(x) or y) and not(w)) or not(z and not(y and w))

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x) or y) and not(w)) or not(z and not(y and w)):
                    None
                else:
                    print(y,x,w,z)

#Видно и без рисунка (На самом деле у меня на arch нету аналога ножниц )