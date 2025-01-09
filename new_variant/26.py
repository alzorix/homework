data = dict()
tasks_big_data = set()
with (open("26.txt") as file):
    trash = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        ID,task = line.split()
        tasks_big_data.add(int(task))
        if ID in data.keys():
            s = data[ID]
            s.add(task)
            data[ID] = s
        else:
            s = set()
            s.add(task)

            data[ID] = s
        line = file.readline().strip()

#print(data)

ansewer = list() # ID и максимальное количество решенных задач
tasks_big_data = list(tasks_big_data)
tasks_big_data.sort()
for ID in data.keys():

    nice_tasks = 0

    tasks = data[ID]
    tasks = list(tasks)
    tasks.sort()
    last_task = -1
    for current_task in tasks:
        kolvo =0
        if last_task == -1:
            last_task = current_task
        else:
            if int(tasks_big_data.index(int(last_task))) +1 == int(tasks_big_data.index(int(current_task))):
                kolvo+=1
            else:
                nice_tasks = max(nice_tasks,kolvo)
                kolvo = 0
    ansewer.append((nice_tasks,int(ID)))

ansewer.sort()
print(max(ansewer))

