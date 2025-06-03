with open("files/24-181.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0

    Y = False
    dot = 0

    for i in  range(len(line)):
        if line[i] == "Y":
            Y = True
        if line[i] == ".":
            dot+=1

        while Y == True or dot > 5:
            if line[smart_start] == "Y":
                Y = False
            if line[smart_start] == ".":
                dot -= 1

            smart_start +=1

        if Y == False and dot <=5:
            max_sequence_char = max(max_sequence_char,i - smart_start +1)
print(max_sequence_char)
