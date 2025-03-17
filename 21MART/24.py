with open("24.txt") as f:
    data = f.readline().strip()

data = data.replace("7","1")
data = data.replace("8","1")
data = data.replace("9","1")
data = data.replace("-","*")

data=data.split("*")

global_len = 0
local_len = 0


for podline in data:
    if podline  != "" and (podline[0] != "0" or podline == "0"):
        local_len += len(podline) +1
        global_len = max(global_len, local_len-1)
    elif podline !="" and podline[0] == "0":

        global_len = max(global_len, local_len + 1)

        search = podline.find("1")
        if search != -1:
            local_len = len(podline[search::]) +1
            global_len = max(global_len, local_len - 1)
        else:

            local_len = 0
    else:
        local_len = 0
print(global_len)

#109
#Ошибка была найдена при сравнении с другим рещением,по этому не считается.
# При этом ошибку можно обнаружить проверяя логику программы,что возможно на экзамене.

'''    elif podline !="" and podline[0] == "0":

        global_len = max(global_len, local_len + 1)'''
#Я тут рефлекторно написал local_len - 1


#111