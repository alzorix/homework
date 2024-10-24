with open("files/24-280.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0

    Z = 0
    Y = 0
    X = 0
    A= False
    B = False
    C = False


    for i in range(len(line)):
        if line[i] == "Z":
            Z +=1

        if line[i] == "Y":
            Y +=1

        if line[i] == "X":
            X +=1

        if line[i] == "A":
            A = True
        if line[i] == "B":
            B = True
        if line[i] == "C":
            C = True

        while X > 5 or Y > 5 or Z > 5 or A or B or C:
            if line[smart_start] == "X":
                X -= 1

            if line[smart_start] == "Y":
                Y -=1

            if line[smart_start] == "Z":
                Z -=1

            if line[smart_start] == "A":
                A = False
            if line[smart_start] == "B":
                B = False
            if line[smart_start] == "C":
                C = False


            smart_start+=1
        if X ==5 and Y ==5 and Z ==5 and (not(C)) and (not(A)) and (not(B)):
            max_sequence_char = max(max_sequence_char,i+1-smart_start)

print(max_sequence_char)

