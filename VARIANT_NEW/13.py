import ipaddress

net = ipaddress.ip_network("111.194.0.0/255.254.0.0",strict=False)

IPs = [p for p in net.hosts()]
c =0
for x in IPs:
    #print(x)
    x = f'{x:b}' #Забыл эту запись
    if (x.count("1") - x.count("0"))%2 ==0:
        c +=1
print(c)#131070