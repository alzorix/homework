data = list()
max_ysl = 0

def ysl(n:str):
    return len(str(abs(int(n)))) == 5 and n[-2:] == "43"
with open("17.txt") as file:
    line = file.readline().strip()
    while line !="":
        data.append(line)
        if ysl(line):
            max_ysl = max(max_ysl,int(line))
        line = file.readline().strip()

max_ysl = max_ysl * max_ysl


ans = list()
for index in range(len(data)-2):
    a = data[index]
    a1 = data[index+1]
    a2 = data[index+2]

    if ysl(a) or   ysl(a1) or     ysl(a2):
        a = int(a)
        a1 = int(a1)
        a2 = int(a2)
        x =  (a*a +    a1*a1 +   a2*a2)
        if not(  x> max_ysl ):
            ans.append(x)
print(len(ans),min(ans))

