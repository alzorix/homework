
elements = list()


with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":
        elements.append(line)
        line = file.readline().strip()
max_pairs = -float("inf")
for id in range(len(elements)-1):
    if (len(elements[id]) == 2 and len(elements[id+1]) != 2) or (len(elements[id+1]) == 2 and len(elements[id]) != 2):
        t = int(elements[id]) + int(elements[id+1])
        if max_pairs <= t:
            max_pairs = t

ansewers = list()


for element in elements:
    element = int(element)
    if element > max_pairs:
        ansewers.append(element)
print(len(ansewers),min(ansewers))