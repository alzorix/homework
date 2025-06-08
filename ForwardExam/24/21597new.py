with open("24_21597.txt") as file:
    line = file.readline().strip()


line = line.replace("6","!")
line = line.replace("7","!")
line = line.replace("8","!")
line = line.replace("9","!")

line = line.replace("**","!")
line = line.replace("-*","!")
line = line.replace("*-","!")
line = line.replace("--","!")
data = line.split("!")
m = 0

for six_line in data:
    six_line = six_line.strip("*-") #01-011-00111*01
    if six_line != "" and len(six_line) > m:
        for l in range(0, len(six_line) - 1):
            if six_line[l] not in "*-":
                for r in range (l + m + 1, len(six_line)):
                    s = six_line[l:r+1]
                    if s[-1] not in '*-':
                       if s.count('*') > 0 or s.count('-') > 0:
                           rf = s.rfind('*')
                           rl = s.find('-')
                           if rf == -1 or rl == -1 or rf < rl:
                               ss = s.replace('-', '*')
                               ss = ss.split('*')
                               k = 0
                               for i in ss:
                                   if i == '' or len(i) > 1 and i[0] == '0':
                                       k = 1
                                       break
                               if k == 0:
                                   m = max(m, len(s))

print(m)

