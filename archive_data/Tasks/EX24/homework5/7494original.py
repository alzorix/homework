with open("files/24-295.txt") as file:
    line = file.readline().strip()
    smart_start = 0
    max_sequence_char = 0
    DE = 0
    for i in range(len(line)-1):
        if line[i]+line[i+1] == "DE":
            DE +=1


        while DE > 240:
            if line[smart_start]+line[smart_start+1] == "DE":
                DE -=1

            smart_start+=1

        if DE <241:

                max_sequence_char = max(max_sequence_char, i +1 - smart_start + 1)
    print(max_sequence_char)


    #print(line[len(line)-2] + line[len(line)-1])




print(max_sequence_char)
# 1792
