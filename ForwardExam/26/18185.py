
data = dict()
seans = list()
with open("26_18185.txt") as file:
    N,K = file.readline().strip().split()
    line = file.readline().strip()
    while line !="":
        try:
            number_school,number_class,students_count = map(int,line.split())
            if number_class not in data.keys():
                data[number_class] = dict()
                data[number_class][number_school] = students_count
            else:
                if number_school not in  data[number_class].keys():
                    data[number_class][number_school] = students_count
                else:
                    data[number_class][number_school] +=students_count
        except:
            seans.append(int(line))

        line = file.readline().strip()
# на один сеанс могут попасть ученики только одной параллели одной школы

print(data)
seans.sort()
print(seans)
import bisect

count_parallels = 0
total_students = 0

parallel_ids = data.keys()
parallel_ids = list(parallel_ids)
parallel_ids.sort(reverse=True)
for parallel_id in parallel_ids:
    school_ids =  data[parallel_id].keys()
    school_ids = list(school_ids)
    school_ids.sort()
    for school_id in school_ids:
        students = data[parallel_id][school_id]
        for id in range(len(seans)):
            if seans[id] >= students:
                count_parallels +=1
                total_students +=students
                seans.pop(id)
                break



print(count_parallels, total_students)
#3209 73122
