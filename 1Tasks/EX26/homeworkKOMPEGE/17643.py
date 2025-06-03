
#определяем ср цену
database_dict = dict()
prices = list()

with open("26_17643.txt") as file:
    kolvo_tovara = file.readline().strip()

    line = file.readline().strip()

    while line !="":
        article,price,status = line.split()
        if article not in prices:

            prices.append(int(price))
        line = file.readline().strip()

    file.close()





sr_ckass = sum(prices)//len(prices)
#print(sr_ckass)

#Нам нужен список дорогих товаров:с продажами,ценой,остатки,артикулом.


database_dict = dict()
prices = list()

with open("26_17643.txt") as file:
    kolvo_tovara = file.readline().strip()

    line = file.readline().strip()

    while line !="":
        article,price,status = line.split()
        status = int(status)

        if int(price) > sr_ckass:

         if article not in database_dict:
            if status:

                database_dict[article] = ((0,int(price),1,article)) #Товар не продан
                prices.append(int(price))
            else:
                database_dict[article] = ((1,int(price),0,article))#Товар продан
                prices.append(int(price))
         else:


            sale,price,sklad,art = database_dict.get(article)
            sale = int(sale)
            price=int(price)
            sklad=int(sklad)




            if status:
                database_dict[article] = ((sale + 0,price,sklad+1,article))
            else:
                #print(23123)
                database_dict[article] = ((sale + 1,price,sklad+0,article))

                break

        line = file.readline().strip()
    file.close()

rum = list(database_dict.values())
rum.sort()
#print(rum)



sale,price,sklad,art = max(rum)

print(sale*price,sklad)

#print(max(rum))