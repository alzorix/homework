from ipaddress import *
a = ip_network("203.68.128.0/255.255.192.0")
c = 0
for ip in a: #забыл как перевести в двоичн представление нормалньо

    s = str(ip)
    s = s.split(".")
    t = list()
    for x in s:
        t.append(bin(int(x))[2::])
    s = "".join(t)

    if s.count("1") % 7 !=0:
        c+=1



print(c)
#13367
