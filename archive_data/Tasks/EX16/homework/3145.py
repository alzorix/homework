def F(n,m):
 if m == 0:
  d = 0
 else:
  d = n + F(n,m-1)
 return d
t = set()
for x in range(0,200):
    for m in range(0,200):
        if F(x,m) == 30:
            t.add(x)
print(len(t))
#8
