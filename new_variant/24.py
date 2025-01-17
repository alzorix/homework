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
            max_line_dlina = max(max_line_dlina,i +3 - smart_start + 1)
print(max_line_dlina)


# 2379