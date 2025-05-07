from dataclasses import dataclass, field

end_time = 0
max_repair = 0
utilization =0
@dataclass
class item():
    go_time : int
    fix_time:int
    number_master:int

@dataclass
class masterC():
    queue : list
    number_master:int
    repeir_count: int

    def check(self, current_time):

        new_queue = []
        for task in self.queue:
            if current_time < task.go_time + task.fix_time:
                new_queue.append(task)
            else:
                self.repeir_count += 1
                global max_repair
                max_repair = max(max_repair, self.repeir_count)
        self.queue = new_queue

    def add(self, item):
        global utilization
        if len(self.queue) < 5:
            self.queue.append(item)
        else:
            utilization += 1


database = list()
max_master = 0
with open("26.txt") as file:
    trash = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        start,time,master = line.split()
        current_item = item(go_time=int(start),fix_time=int(time),number_master=int(master))
        max_master = max(max_master,int(master))
        end_time = max(end_time,int(start)+int(time))
        database.append(current_item)
        line = file.readline().strip()


database.sort(key = lambda x:( x.go_time,   x.fix_time,  x.number_master    ))

masters = dict()
for x in range(1,max_master+1):
    new_queue = list()
    local_master = masterC(queue = new_queue,number_master=x+1,repeir_count=0)
    masters[x] = local_master


for current_time in range(end_time+10):
    print(masters)
    for x in masters.keys():
        masters[x].check(current_time=current_time)





    if len(database) != 0:
        if current_time == database[0].go_time:
            new_item = database.pop(0)

            if new_item.number_master !=0:
                masters[new_item.number_master].add(item=new_item)

            if new_item.number_master ==0:
                temp = list()
                for x in masters.items():
                    temp.append(len(x[1].queue))
                temp_min = min(temp)

                for x in masters.keys():
                    if len(masters[x].queue) == temp_min:
                        masters[x].add(new_item)














    else:
        print("Конец рабочего дня")
        break

print(utilization,max_repair)