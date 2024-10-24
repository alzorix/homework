with open("files/24-280.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0

    A   = 0
    E   = 0
    I   = 0
    O   = 0
    U   = 0
    Y   = 0





    for i in range(len(line)):
        if line[i] == "A":
            A +=1
        if line[i] == "E":
            E +=1
        if line[i] == "I":
            I +=1
        if line[i] == "O":
            O +=1
        if line[i] == "U":
            U +=1
        if line[i] == "Y":
            Y +=1






        while A > 8 or E > 8 or I > 8 or O > 8 or U > 8 or Y > 8:
            if line[smart_start] == "A":
                A -= 1
            if line[smart_start] == "E":
                E -= 1
            if line[smart_start] == "I":
                I -= 1
            if line[smart_start] == "O":
                O -= 1
            if line[smart_start] == "U":
                U -= 1
            if line[smart_start] == "Y":
                Y -= 1

                
            smart_start+=1
        if A == 8 and E == 8 and I == 8 and O == 8 and U == 8 and Y == 8:
            max_sequence_char = max(max_sequence_char,i+1-smart_start)

print(max_sequence_char)

