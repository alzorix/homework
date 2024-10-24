one = True
fist_minimum=None

all_distances = list()
with open("3349") as s:

    line = s.readline().strip()

    for l in range(len(line)-1):
        if one:
            one = False
        else:
            if l == len(line)-1:
                None
            else:

                if ord(line[l]) < ord(line[l-1]) and ord(line[l])< ord(line[l+1]):
                    if fist_minimum == None:
                        fist_minimum = l
                    else:
                        last_minimum = l
                        all_distances.append(last_minimum-fist_minimum)
                        fist_minimum = l


print(max(all_distances))



