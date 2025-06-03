
#определяем ср цену
database_dict = dict()
prices = list()

with open("26-152") as file:
    kolvo_tovara = file.readline().strip()

    line = file.readline().strip()

    while line !="":
        article,price,status = line.split()

        prices.append(int(price))



        line = file.readline().strip()

    file.close()





sr_ckass = sum(prices)/len(prices)
print(sr_ckass)

#Нам нужен список дорогих товаров:с продажами,ценой,остатки,артикулом.


database_dict = dict()

with open("26-152") as file:
    kolvo_tovara = file.readline().strip()

    line = file.readline().strip()

    while line !="":
        article,price,status = line.split()
        status = int(status)

        if int(price) > sr_ckass:

         if article not in database_dict:
            if status:

                database_dict[article] = ((0,int(price),-1,article)) #с продажами,ценой,остатки,артикулом.
            else:
                database_dict[article] = ((1,int(price),0,article)) #с продажами,ценой,остатки,артикулом.
         else:

            sale,price,sklad,art = database_dict.get(article)

            if status:
                database_dict[article] = ((sale,int(price),sklad-1,article))
            else:
                database_dict[article] = ((sale + 1,int(price),sklad,article))


        line = file.readline().strip()
    file.close()

rum = database_dict.values()



sale,price,sklad,art = max(rum)
print(rum)

print(sale*price,abs(sklad)) #0 47

#print(max(rum))