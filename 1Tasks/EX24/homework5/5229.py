with open("files/24-1.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    max_sequence_char = 0


    test_all = 0

    for i in range(len(line)):
        if line[i] == "A":

            test_all +=1
        if line[i] == "B":

            test_all +=1
        if line[i] == "X":

            test_all +=1
        while  test_all>5:
            if line[smart_start] == "X":
                #X -= 1
                test_all -=1
            if line[smart_start] == "B":
                #B -=1
                test_all -=1
            if line[smart_start] == "A":
                #A -=1
                test_all -=1
            smart_start+=1
        if  test_all<6:
            max_sequence_char = max(max_sequence_char,i+1-smart_start)

print(max_sequence_char)


