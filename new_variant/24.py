with open("24.txt") as file:
    line = file.readline().strip()

    smart_start = 0
    FSRQ = 0
    max_line_dlina =0

    for i in range(len(line) - 3):
        if line[i] + line[i+1] + line[i+2] +line[i+3] == "FSRQ":
            FSRQ+=1


        while FSRQ >80:
            if line[smart_start] + line[smart_start+1] + line[smart_start+2] +line[smart_start+3] == "FSRQ":
                FSRQ-=1
            smart_start+=1

        if FSRQ == 80:
            max_line_dlina = max(max_line_dlina,i +1 - smart_start + 1)
print(max_line_dlina)


with open("24.txt") as file:
    line = file.readline().strip()
    smart_start = 0
    max_sequence_char = 0
    DE = 0
    for i in range(len(line)-3):
        if line[i] + line[i + 1] + line[i + 2] + line[i + 3] == "FSRQ":
            DE +=1


        while DE > 80:
            if line[smart_start] + line[smart_start+1] + line[smart_start+2] +line[smart_start+3] == "FSRQ":

                DE -=1

            smart_start+=1

        if DE ==80:

                max_sequence_char = max(max_sequence_char, i +1 - smart_start + 1)



    #print(line[len(line)-2] + line[len(line)-1])




print(max_sequence_char)

# 2377
# 2377
