with open("files/24-298.txt") as file:
    line = file.readline().strip()
    smart_start = 0
    max_sequence_char = 0
    count_line = ""

    CD = 1

    for i in range(len(line)):
        last_line = count_line

        try:
            a = eval(f"{count_line + line[i]}")
            count_line = count_line + line[i]
        except:
            max_sequence_char = max(max_sequence_char, len(count_line))

            print(count_line)
            if last_line == count_line:
                count_line= ""



print(max_sequence_char)