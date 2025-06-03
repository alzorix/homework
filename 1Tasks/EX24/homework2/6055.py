

start_ananlyze = None
fist = True
str_all = list()

def analyze(object:str):
    if object.count("E") >= 5:
        fitr = True

        start_E_index = None
        doptest= 0
        for i in range(len(object)):
            if object[i] == "E":
                if fitr:
                    start_E_index = i +1
                    fitr = False
                else:
                    end_E_index = i
                    small_object = object[start_E_index:end_E_index]
                    if small_object.count("A") ==1:
                        doptest+=1



                    else:
                        #print(small_object)
                        return False
                    #fitr = True
                    start_E_index = i + 1


        if doptest ==object.count("E")-1:
                return True
        else:
            return False




    return False







with open("6055") as lines:
    line = lines.readline().strip()
    for l in  range(0,len(line)):
        if line[l] =="F":
            if fist:
                start_ananlyze = l+1
                fist = False
            else:
                end_ananlyze = l
                object_analyze = line[start_ananlyze:end_ananlyze]
                if analyze(object_analyze):

                    str_all.append(len(object_analyze)+2)
                start_ananlyze = l + 1
                #fist = True
print(max(str_all))








