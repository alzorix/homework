from dataclasses import dataclass

@dataclass
class item():
    go_time : int
    fix_time:int
    number_master:int
database = list()
with open("26.txt") as file:
    trash = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        start,time,master = line.split()
        current_item = item(go_time=int(start),fix_time=int(time),number_master=int(master))
        database.append(current_item)
        line = file.readline().strip()

max_repair = 0
utilization =0
database.sort(key = lambda x:( x.go_time,   x.fix_time,  x.number_master    ))
print(database)

