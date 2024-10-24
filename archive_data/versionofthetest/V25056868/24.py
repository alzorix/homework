with open("24.txt") as file:
    line = file.readline().strip()
    smart_start = 0
    max_sequence_char = 0

    CD = 0

    for i in range(len(line)-1):


        if line[i]+line[i+1] == "CD":
            CD +=1

        while CD > 160:
            if line[smart_start]+line[smart_start+1] == "CD":
                CD -=1
            smart_start+=1
        if CD ==160:

                max_sequence_char = max(max_sequence_char, i+1 - smart_start + 1)

print(max_sequence_char)
