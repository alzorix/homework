'''(№ 7850) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
 какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети.
  Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и его маске.
   Узлы с IP-адресами 126.115.78.15 и 126.115.84.26 принадлежат одной сети. Какое наименьшее количество IP-адресов,
    в двоичной записи которых ровно 22 единицы, может содержаться в этой сети? '''

from ipaddress import ip_network
ip1 = "126.115.78.15"
ip2="126.115.84.26"

for mask in range(31,15,-1):
    net1=ip_network(f'{ip1}/{mask}',0)

    net2=ip_network(f'{ip2}/{mask}',0)


    if net1.network_address == net2.network_address:
        l_count = 0
        for i in net1.hosts():
            if f'{i:b}'.count("1") == 22:
                l_count+=1

        print(l_count)


