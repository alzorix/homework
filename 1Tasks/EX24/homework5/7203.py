with open("files/24-280.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0

    S = 0
    U = 0
    N = 0
    X= False
    Y = False



    for i in range(len(line)):
        if line[i] == "S":
            S +=1

        if line[i] == "U":
            U +=1

        if line[i] == "N":
            N +=1

        if line[i] == "X":
            X = True
        if line[i] == "Y":
            Y = True


        while S > 10 or U > 10 or N > 10 or X or Y:
            if line[smart_start] == "S":
                S -= 1

            if line[smart_start] == "U":
                U -= 1

            if line[smart_start] == "N":
                N -= 1

            if line[smart_start] == "X":
                X = False
            if line[smart_start] == "Y":
                Y = False

            smart_start+=1
        if S <11 and U <11 and N <11 and (not(X)) and (not(Y)):
            max_sequence_char = max(max_sequence_char,i+1-smart_start)

print(max_sequence_char)

