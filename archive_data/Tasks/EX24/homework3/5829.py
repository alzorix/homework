C = dict()


with open("5829") as lines:
    line = lines.readline().strip()
    for l in  range(0,len(line)-2):
        if line[l] =="X" and line[l+2] =="P":
            if line[l+1]  not in C:
                C[line[l+1]] = 1
            else:
                C[line[l + 1]]  +=1
sorted_C = sorted(C)

highest_number_of_repetitions = 0
the_largest_letter_in_the_alphabet = None

for i in sorted_C:
    if C[i] > highest_number_of_repetitions:
        highest_number_of_repetitions =  C[i]
        the_largest_letter_in_the_alphabet = i


print(f"{highest_number_of_repetitions}")

