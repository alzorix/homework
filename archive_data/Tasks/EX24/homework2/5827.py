




t = list()
fist = True
start_index= None
with open("5827") as lines:
    line = lines.readline().strip()

    for l in  range(len(line)):
        if line[l].isdigit():
            if fist and line[l] != "0":
                if line[l-1] !="0":
                    start_index = l
                    fist = False
        else:
            if fist == False:
                object_analyze = line[start_index:l]
                t.append(int(object_analyze))

                fist = True

    if fist == False:
            object_analyze = line[start_index:l]
            t.append(int(object_analyze))

            fist = True


print(max(t))








