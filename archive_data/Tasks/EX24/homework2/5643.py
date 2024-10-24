
from fnmatch import fnmatch


start_ananlyze = None
fist = True
str_all = list()


def analyzer(line:str):
        try:


            st = line.find("12")


            if line[st+6] =="7" and  line[st+7] == "7":
                if line[st+10] == "9":
                    test = line[st:st+11]
                    for i in test:
                        if i.isdigit():

                            None
                        else:
                            return False


                    return (True,test)
        except:
            None
        return (False,"")



def goodansawer(object):
    chet = 1
    nichet = 0
    for simbol in object:
        simbol = int(simbol)
        if simbol %2 ==0:
            chet = chet*simbol
        else:
            nichet +=simbol
    return  nichet+chet







with open("5643") as lines:
    line = lines.readline().strip()
    for l in  range(0,len(line)-1):

        if line[l:l+2] =="SS":
            if fist:
                start_index_ananlyze = l+2
                fist = False
            else:
                object_analyze = line[start_index_ananlyze:l]
                if analyzer(object_analyze)[0]:
                    #print(object_analyze,analyzer(object_analyze))


                    str_all.append(goodansawer(analyzer(object_analyze)[1]))




                fist = True





print(max(str_all))


#Непр ответ