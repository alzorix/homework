from itertools import product
ansewer = 0
c = 0
for notans in product("АВНРЬЯ",repeat =5):
    c+=1
    ans = "".join(notans)
    if ans[0] != "Я":
        if ans.count("Ь") <=1:
            if "ЯЯ" not in ans:
                ansewer = c
print(ansewer)
#6406
