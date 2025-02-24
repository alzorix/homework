ss = list()
for N in range(40000):
    octN = oct(N)[2::]
    if int(octN) % 2 == 0:
        s = ""
        for x in octN:
            if int(x)% 2 ==0:
                s += x
            else:
                s += "2"
        octN = s
    else:
        octN = "3"+ octN[1:-1] + "3"
    R = int(octN,8)
    ss.append(R)
print(max(ss))
