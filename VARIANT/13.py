import ipaddress
#Кратко повторить структуру и команды

ip = ipaddress.ip_network("98.81.154.195/255.252.0.0",strict=False)

print(str(max(ip.hosts())).replace(".",""))