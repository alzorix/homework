'''(№ 7047) *(М. Ишимов) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
 какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
  Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
  Сеть, в которой содержится узел с IP-адресом 227.31.A.139, задана маской сети 255.255.255.224,
   где A – некоторое допустимое для записи IP-адреса число. Определите максимальное значение A,
    для которого для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное количество нулей в левых двух байтах
     не больше суммарного количества нулей в правых двух байтах. '''


from ipaddress import ip_network

for A in range(0,256):

        net = ip_network(f"227.31.{A}.139/255.255.255.224",0)
        Flag = True

        for ip in net:


            lev = f"{ip:b}"[:16]
            prav = f"{ip:b}"[16:]

            if lev.count("0")  <= prav.count("0"):
                None
            else:
                Flag = False



        if Flag:
            print(A)

# Опять неверно