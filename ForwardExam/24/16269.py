with open("24_16269.txt") as file:
    line = file.readline().strip()
blackline = "TUVW"
s = list()
for n in line:
    if n in blackline:
        s.append("!")
    else:
        s.append(n)
line = "".join(s)
while "XXXX" in line:
    line = line.replace("XXXX","XX!XX")
while "YYYY" in line:
    line = line.replace("YYYY","YY!YY")
while "ZZZZ" in line:
    line = line.replace("ZZZZ","ZZ!ZZ")

while "XXX" in line:
    line = line.replace("XXX","XX!XX")
while "YYY" in line:
    line = line.replace("YYY","YY!YY")
while "ZZZ" in line:
    line = line.replace("ZZZ","ZZ!ZZ")

line = line.replace("XX","**")
line = line.replace("YY","**")
line = line.replace("ZZ","**")
line = line.replace("X","!")
line = line.replace("Y","!")
line = line.replace("Z","!")
line = line.split("!")
print(max([len(p) for p in line]))
# ans = 0
# for local in line:
#     if local!="":
#         c = 0
#         Fist = True
#         print(local)
#         x = 0
#         while x <len(local)-3:
#             XX = local[x] +  local[x+1]
#             YY = local[x+2] +  local[x+3]
#             T = 1
#             if local[x] !=  local[x+1]:
#                 T = 0
#             if local[x+2] !=  local[x+3]:
#                 T = 0
#             if T==0:
#                 print("T=0")
#                 print(XX, YY)
#                 ans = max(ans, c)
#
#                 x += 1
#                 c = 0
#                 Fist = True
#                 continue
#
#
#             if XX != YY:
#                 if Fist:
#                     c+=4
#                     Fist = False
#                     x+=2
#                 else:
#                     c+=2
#                     x += 2
#             else:
#                 print("UPD ANS",c,x)
#                 print(XX, YY)
#                 ans = max(ans,c)
#                 x += 1
#                 c = 0
#                 Fist = True
# ans = max(ans, c)
# print(ans)

