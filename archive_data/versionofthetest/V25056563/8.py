alfabet_1 = [ "3",    "5",      "7"    ]
alfabet_2 = [ "0",  "2",    "4",      "6"    ]


count = 0
for a1 in alfabet_1:
    for a2 in alfabet_2:
        for a3 in alfabet_1:
            for a4 in alfabet_2:
                for a5 in alfabet_1:
                    line = a1+a2+a3+a4+a5
                    if line.count("0") <=1:
                            if line.count("2") <= 1:
                                if line.count("3") <= 1:
                                    if line.count("4") <= 1:
                                        if line.count("5") <= 1:
                                            if line.count("6") <= 1:
                                                if line.count("7") <= 1:

                                                    count+=1
for a1 in alfabet_2:
    for a2 in alfabet_1:
        for a3 in alfabet_2:
            for a4 in alfabet_1:
                for a5 in alfabet_2:
                    line = a1+a2+a3+a4+a5
                    if line.count("0") <=1:
                            if line.count("2") <= 1:
                                if line.count("3") <= 1:
                                    if line.count("4") <= 1:
                                        if line.count("5") <= 1:
                                            if line.count("6") <= 1:
                                                if line.count("7") <= 1:
                                                    count+=1
print(count) #  Получается ответ 216,заместо 180

