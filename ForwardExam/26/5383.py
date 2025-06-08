data = list()
vse_knigi_vagnie = list()
with open("26_5383.txt") as file:
    N,S = map(int,file.readline().strip().split())
    line = file.readline().strip()
    while line !="":
        kolvo,flag = map(int,line.split())
        if flag:
            vse_knigi_vagnie.append(kolvo+10)
        else:
            data.append((kolvo+10))
        line = file.readline().strip()

'''какое максимальное количество книг Петя сможет поставить на нижней полке при условии, 
что все обязательные книги поставлены, 
а так же количество страниц в самой большой книге среди необязательных,
 которую можно поставить на нижнюю полку при условии,
  что на нижней полке размещено максимальное количество книг и все обязательные книги поставлены.'''

max_books = 0
S = S - sum(vse_knigi_vagnie)
data.sort(reverse=True)
neob_na_polke = list()
while min(data) <=S and S >0:
    t = data.pop()
    neob_na_polke.append(t)
    S-=t
#print(data)
print(len(vse_knigi_vagnie)+len(neob_na_polke))
# neob_na_polke.sort(reverse=True)
# print("НЕОБ попавшие:")
# print(neob_na_polke)
# data.sort(reverse=True)
# print("НЕОБ непопавшие:")
# print(data)
# print("лимит:")
# print(S)
# print("Всего есть:")
print(max(neob_na_polke)+ S-10) #-10 обложка. Проверку писать было лень,посмотрел руками
#1566 78