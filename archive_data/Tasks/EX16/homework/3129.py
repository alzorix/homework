def F( n ):
  ans = list()
  ans.append(1)
  if n >= 1:
    ans.append(1)
    ans = ans + F(n-1)
    ans = ans + F(n-2)
    ans.append(1)
  return ans

print(len(F(35)))
#96631265
#можно реализовать через int