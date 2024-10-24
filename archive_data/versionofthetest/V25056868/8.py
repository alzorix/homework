#Не помню, чтобы я такой тип заданий делал.

start_digital = [2,4,6]
end_digital = [0,1,3,4,5,7]

start_digital = list(map(str,start_digital))
end_digital = list(map(str,end_digital))


seredina = [1,2,3,4,5,6,7,0]

seredina = list(map(str,seredina))

#print(start_digital,end_digital,seredina)
count = 0

for a1 in start_digital:
    for a2 in seredina:
        for a3 in seredina:
            for a4 in seredina:
                for a5 in end_digital:
                    line = a1 + a2 + a3 +a4+a5
                    if line.count("7") <3:
                        count+=1
print(count)


#9135