from ipaddress import ip_network
c = 0
net = ip_network("112.160.0.0/255.240.0.0",0)
for ip in net.hosts():
    if f"{ip:b}".count("1") % 5 == 0:
        c+=1

if f"{net.broadcast_address:b}".count("1") % 5 == 0:
    c+=1
if f"{min(net.hosts()) - 1:b}".count("0") > 21:
    c += 1
print(c)
#215766
