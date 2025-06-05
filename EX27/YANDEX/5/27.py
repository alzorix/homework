data_trash = list()

max_sallary_G = 0

NUMBER_FILE="A"
with open("27_A.txt") as file:
    line = file.readline().strip()
    line = file.readline().strip()
    while line !="":
        ID,job_name,company_name,city,min_calary,max_calary,time_job,time_published,Skills = line.split(";")
        FLAG = True

        if ID == "":
            FLAG = False
        if job_name == "":
            FLAG = False
        if company_name == "":
            FLAG = False
        if city == "":
            FLAG = False
        if time_job == "":
            FLAG = False
        if time_published == "":
            FLAG = False
        if Skills == "":
            FLAG = False
        if max_calary != "" and min_calary != "":
            if int(min_calary) > int(max_calary):
                FLAG = False


        if FLAG:
            data_trash.append((ID,job_name,company_name,city,min_calary,max_calary,time_job,time_published,Skills))
        line = file.readline().strip()

data_trash = set(data_trash)
data_trash = list(data_trash)
data = list()


data = []




for line in data_trash:
    ID, job_name, company_name, city, min_calary, max_calary, time_job, time_published, Skills = line
    CR_salary = None
    if max_calary != "" and min_calary != "":
        CR_salary = int((int(max_calary) + int(min_calary)) // 2)

    elif max_calary != "":
            CR_salary = int(max_calary)
    elif min_calary != "":
            CR_salary = int(min_calary)
    else:
        continue

    max_sallary_G = max(max_sallary_G,int(CR_salary)) #В чём смысл ячеек,если в них никто не попадает? Правильно незачем

    inPython = False

    for p in Skills.split(","):
        p = p.replace("[","")
        p = p.replace("]", "")
        p = p.replace(" ", "")
        if p == "Python":
            inPython = True

            break



    data.append((CR_salary,time_job,inPython))
print(len(data))

MSX = max_sallary_G // 50000
n_data = [[[] for _ in range(5)] for _ in range(MSX + 1)]


while len(data) != 0:
    dot = data.pop()
    CR_salary, time_job, Skills = dot
    time_job = int(time_job)
    if 0 <= time_job<= 1:
        group = 0
    if 2 <= time_job<= 3:
        group = 1
    if 4 <= time_job<= 5:
        group = 2
    if 6 <= time_job<= 7:
        group = 3
    if 8 <= time_job <= 9:
        group = 4
    n_data[int(CR_salary //50000)][group].append( dot)
print(n_data)

def get_sosed(cluster):
    sosedi = list()
    x,y = cluster
    otn_coorc = [(-1,0), (1,0), (0,-1), (0,1)]
    for o_x,o_y in otn_coorc:
        sosed_X = x + o_x
        sosed_Y = y + o_y
        if 0<= sosed_X <(max_sallary_G //50000)+1 and 0 <= sosed_Y < 5:
            sosedi.append((sosed_X,sosed_Y))
    return sosedi
MSX = max_sallary_G //50000


ALL_data_ans =list()
for x_cl in range(MSX+1):
    for y_cl in range(5):
        cluster = n_data[x_cl][y_cl]
        sosedi = get_sosed((x_cl,y_cl))

        if NUMBER_FILE == "A":
            for o_cor_cluster in sosedi:
                x,y = o_cor_cluster
                other_cluster = n_data[x][y]

                new_cluster = []
                new_cluster.extend(cluster)
                new_cluster.extend(other_cluster)
                S =0
                K = 0
                for local_data_dolj in new_cluster:
                    _,_,Python = local_data_dolj
                    if Python:
                        S+=1
                    else:
                        K+=1
                ALL_data_ans.append((len(new_cluster),S,K))

_,S,K = max(ALL_data_ans)
print(S,K)
#30 194
#Ответ не верный