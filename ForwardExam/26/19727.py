import itertools

data = list()
with open("26.2_19727.txt") as file:
    Massa,kolvo = map(int,file.readline().strip().split())
    line = file.readline().strip()
    while line != "":
        data.append(int(line))
        line = file.readline().strip()
data_c = data.copy()
bidons=0
ostatok = list()

data.sort(reverse=True)
while len(data)!= 0:
    bidon = data.pop() #т.е. наименьшей
    if bidon<=Massa:
        Massa-=bidon
        bidons+=1
    else:
        ostatok.append(bidon)


#162 838
#Как перебрать  число бидонов, которые заведомо не сможет увезти поезд, при условии,
# что количество погруженных бидонов наибольшее.
# я не помню

def detect(nums,sum_,k): #Как и ожидалось брутфорс долгий
    ans = []
    for x in nums:
        F = False
        candidats = [p for p in nums if p != x]
        for line in itertools.combinations(candidats,k-1):
            if x + sum(line) == sum_:
                F = True
                break
        if not(F):
            ans.append(x)
    return ans

print(bidons,len(detect(data_c,2500,bidons)))