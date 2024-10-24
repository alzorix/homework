with open("files/24-280.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0

    Z = 0
    Y = 0
    X = 0


    for i in range(len(line)):
        if line[i] == "Z":
            Z +=1

        if line[i] == "Y":
            Y +=1

        if line[i] == "X":
            X +=1

        while X > 3 or Y > 3 or Z > 3:
            if line[smart_start] == "X":
                X -= 1

            if line[smart_start] == "Y":
                Y -=1

            if line[smart_start] == "Z":
                Z -=1

            smart_start+=1
        if X <4 and Y < 4 and Z <4:
            max_sequence_char = max(max_sequence_char,i+1-smart_start)

print(max_sequence_char)

