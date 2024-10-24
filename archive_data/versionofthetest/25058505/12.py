def naslos(v:str,line:str)->bool:
    return v in line

def zamenit(v:str,w:str,line:str) ->str:
    return line.replace(v,w,1)

line_input ="1"*81
while naslos("11111",line_input) or naslos("888",line_input):
    if naslos("11111",line_input):
        line_input = zamenit("11111","88",line_input)
    else:

        line_input = zamenit("888", "8", line_input)
print(line_input)