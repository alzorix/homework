database = list()

with open("26.txt") as file:
    line = file.readline().strip()
    porog = int(line) *(1/3)
    while line !="":
        line = file.readline().strip()
        if line !="":
            ID,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 = line.split()

            balance = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)+int(q8)+int(q9)+int(q10)
            temp = [int(q1),int(q2),int(q3),int(q4),int(q5),int(q6),int(q7),int(q8),int(q9),int(q10)]
            plus_balance = 0
            quest_len = 0
            for i in temp:
                if abs(i) == i:
                    plus_balance+=i
                if i != 0:
                    quest_len+=1
            database.append((balance,-plus_balance,-quest_len,int(ID)))

database.sort()
print(int(porog))
print(len(database))
good = database[int(porog)]


for i in range(int(porog),-1,-1):
    database.pop(i)

print(good)

# Почему ошибка возникает?