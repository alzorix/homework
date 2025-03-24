ip1 = "161.137.200.35"
ip2 = "161.137.150.118"

from  ipaddress import  *
for mask in range(31,0,-1):
 l_count = 0
 net1 = ip_network(f"{ip1}/{mask}",0)
 net2 = ip_network(f"{ip2}/{mask}",0)

 if net1.network_address == net2.network_address:
        print(net1.netmask)
#128