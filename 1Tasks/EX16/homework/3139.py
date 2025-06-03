def F(n):
  if n < 10:
    return n
  else:
    m = F(n//10)
    d = m%10;
    if m < d:
      return d
    else:
      return m

for n in range(999,99,-1):
    s = F(n)
    if s>7:
        print(n,s)
        exit()

#999 9
