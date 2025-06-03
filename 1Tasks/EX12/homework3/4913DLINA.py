def dlina(a):
    a =str(a)
    return len(a)
def izvlech(a,i):
    a = str(a)
    return a[i-1]
def skleit(a,b):

    a = str(a) + str(b)
    return a
a = 20*"5"+ 20*"7"
i = 1
s = 1
b = ""
while i < dlina(a):
  if s == 1:
    c = izvlech(a, i)
    s = 0
  else:
    c = izvlech(a, dlina(a) - i)
    s = 1

  b = skleit(b, c)
  i = i + 4
print(b)