A = 0

def itsdveraznai(i):
    for a in range(0, len(i) - 1):
        if int(i[a]) % 2 == int(i[a + 1]) % 2:
            return False
    return True





for i in range(100_000,1_000_000,5):
    i = str(i)
    F = set(i)
    if len(F) == len(i):
        if itsdveraznai(i):
            A +=1
print(A)