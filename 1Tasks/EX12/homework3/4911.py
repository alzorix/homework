def dlina(a):
    a =str(a)
    return len(a)
def izvlech(a,i):
    a = str(a)
    return a[i-1]
def skleit(a,b):

    a = str(a) + str(b)
    return a
a = "КИЛОБИТ"
i = 0
b = ""
while i < dlina(a):
  c = izvlech(a, dlina(a) - i)
  b = skleit(b, c)
  i = i + 1
print(b)