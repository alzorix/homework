data = list()
with open("26_21910.txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        data.append(int(line))
        line = file.readline().strip()
print(len(data))

data.sort(reverse=True)


will_boxes = list([])


last_data = float("inf")
for dlina in data:
    F = True
    for n,box in enumerate(will_boxes):

        minn = min(box)
        if  minn -dlina >=9:
            will_boxes[n].append(dlina)
            F = False
            break
    if F:
        will_boxes.append([dlina])
ans = list()# len(box) min(box)
for x in will_boxes:
    ans.append((len(x),min(x)))
ans.sort(reverse=True)
print(ans)

print(max(ans))