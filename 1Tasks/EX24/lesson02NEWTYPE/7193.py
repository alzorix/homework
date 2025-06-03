with open("7193") as file:
    line = file.readline().strip()

    left = 0
    max_str = 0

    X = 0
    Y = 0

    for i in range(len(line)):
        if line[i] == "X":
            X+=1
        if line[i] == "Y":
            Y+=1

        while X > 1 or Y > 1:
            if line[left] == "X":
                X = X -1
            if line[left] == "Y":
                Y = Y -1

            left +=1
        if X == 1 and Y == 1:
            max_str = max(max_str,i - left + 1)
print(max_str)

#FXGHFXGHXHUIUYYKJHXHFGYX




