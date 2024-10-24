def nashlos(line:str,v:str):
    if v in line:
        return True
    else:
        return False
def zamenit(line:str,v:str,w:str):
    return line.replace(v,w,1)


input_line = 81 * "9"
while nashlos(input_line,"33333") or nashlos(input_line,"999"):
    if nashlos(input_line,"33333"):
        input_line = zamenit(input_line,"33333","99")
    else:
        input_line = zamenit(input_line, "999", "3")
print(input_line)
#3
