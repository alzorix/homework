alfabet = ["0","1","2","3","4","5","6","7","8","9","A","B"]
count =0
for a1 in alfabet:
    for a2 in alfabet:
        for a3 in alfabet:
            for a4 in alfabet:
                for a5 in alfabet:

                    line = a1+a2+ a3+a4+a5
                    if line[0] != "0":
                        if line.count("7") ==1:
                            if line.count("9") +line.count("A") +line.count("B")  <=3:
                                count+=1
print(count)
