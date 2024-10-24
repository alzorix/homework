ALFABET = "0 1 2 3 4 5 6 7 8 9 A B C D".split(" ")
ALFABET_START = "1 2 3 4 5 6 7 8 9 A B C D".split(" ")
Count_lines = 0
for a1 in ALFABET_START:
    for a2 in ALFABET:
        for a3 in ALFABET:
            for a4 in ALFABET:
                for a5 in ALFABET:
                    line = str(a1+a2+a3+a4+a5)
                    if line.count("9") == 1:
                        if line.count("B") +line.count("C") + line.count("D") <4:
                            Count_lines+=1
print(Count_lines)
#132737

