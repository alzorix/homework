from ipaddress import ip_network
c = 0
net = ip_network("106.184.0.0/255.248.0.0",0)
for ip in net.hosts():
    if f"{ip:b}".count("1") % 2 != 0:
        c+=1
if f"{net.broadcast_address:b}".count("1") % 2 != 0:
    c+=1

print(c)
#262144
