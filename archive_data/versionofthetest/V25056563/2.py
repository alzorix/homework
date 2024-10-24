# F = (not(y<=w)) or (x<=z) or (not(x))

print("X Y W Z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=w)) or (x<=z) or (not(x)):
                    None
                else:
                    print(x,y,w,z)
#XYZW