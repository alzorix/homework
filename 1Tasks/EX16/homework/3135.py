def F( n ):
  ans = list()
  ans.append(2*n+1)
  if n > 1:
    #print(3*n-8)
    ans.append(3*n-8)
    ans = ans + F(n-1) + F(n-4)
  return ans

for n in range(-10,1000):
    res = F(n)
    s = sum(res)
    if s > 5000000:
        print(n,s)
        exit()

#40 6791973