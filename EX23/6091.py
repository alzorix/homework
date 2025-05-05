one ="-333132321454523"
two = "-142721232343432"

results = list()
def F(start,end,history:str="",energy=0,count=1):
    if count >= 15:
        return 0
    if start == end:
        results.append((energy,history))
        return 1
    if start>=end:
        return 0
    else:
        return F(start+1,end,history+"1",energy+int(one[count]),count+1) + F(start*2,end,history+"2",energy+int(two[count]),count+1)

print(F(1,16))

print(min(results))
#3