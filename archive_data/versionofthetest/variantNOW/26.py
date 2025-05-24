from dataclasses import dataclass

end_time = 0
max_repair = 0
utilization =0
@dataclass
class item():
    go_time : int
    fix_time:int
    number_master:int
@dataclass
class Task():
    fix_end_time : int
@dataclass
class masterC():
    queue : list[Task]
    repeir_count: int = 0

    def check(self, current_time):

        new_queue = []
        for task in self.queue:
            if current_time < task.fix_end_time:
                new_queue.append(task)
            else:
                self.repeir_count += 1
                global max_repair
                max_repair = max(max_repair, self.repeir_count)
        self.queue = new_queue

    def add(self, item):
        global utilization
        if len(self.queue) < 5:
            if len(self.queue) !=0:
                new_time = max(self.queue[-1].fix_end_time ,item.go_time )+   item.fix_time
            else:
                new_time =  item.fix_time + item.go_time
            new_task = Task(fix_end_time=new_time)
            self.queue.append(new_task)
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
    repeir_count = 0
    local_master = masterC(queue = new_queue,repeir_count=repeir_count)
    masters[x] = local_master


for current_time in range(end_time+1000000):
    for x in masters.keys():
        masters[x].check(current_time=current_time)






    if len(database) != 0:
        if current_time == database[0].go_time:
            new_item = database.pop(0)

            if new_item.number_master !=0:
                masters[new_item.number_master].add(item=new_item)

            else:
                temp = list()
                for x in masters.items():
                    temp.append(len(x[1].queue))
                temp_min = min(temp)

                for x in masters.keys():
                    if len(masters[x].queue) == temp_min:
                        masters[x].add(new_item)
                        break



print(masters)
print(max_repair,utilization)
#72 218
