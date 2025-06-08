data = dict()

with open("26_21719(1).txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()
    while line != "":
        ID, number = map(int, line.split())
        if ID not in data.keys():
            data[ID] = [number]
        else:
            data[ID].append(number)
        line = file.readline().strip()
print(data)
ansewers = list()
for ID in data.keys():
    tasks = data[ID]
    tasks = set(tasks)
    tasks = list(tasks)
    tasks.sort()
    print(tasks)
    YSLs = 1 #За счёт начала последовательности мы тут пишем?
    for task_id in range(len(tasks) - 1):
        task1 = tasks[task_id]
        task2 = tasks[task_id + 1]
        if task2 - task1 == 2:
            YSLs += 1
        else:
            ansewers.append((YSLs, -ID))
            YSLs = 1
        ansewers.append((YSLs, -ID))


print(max(ansewers))

#10135 42