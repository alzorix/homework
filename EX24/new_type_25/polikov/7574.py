'''(№ 7574) (ЕГЭ-2024) Текстовый файл 24-300.txt состоит не более чем из 106 символов и содержит только десятичные цифры,
 а также знаки «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности,
  являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака), значение которого равно нулю.
   В этом выражении никакие два знака арифметических операций не стоят рядом, порядок действий определяется по правилам математики.
    В записи чисел отсутствуют незначащие (ведущие) нули. В ответе укажите количество символов в найденном выражении. '''


with open("7574") as file:
    line = file.readline().strip()

src_line = line.replace("++","X")
src_line = src_line.replace("+*","X")
src_line = src_line.replace("*+","X")
src_line = src_line.replace("**","X")

max_len =0


for LINE  in src_line.split("X"):
    if len(LINE) > max_len:
        for id_line in range(len(LINE)-1):
            if LINE[id_line]!="+" and LINE[id_line]!="*" and not (LINE[id_line] == "0" and LINE[id_line+1].isdigit()):
                current_line = LINE[id_line]
                for recombinate_line in range(id_line+1,len(LINE)):
                    current_line+= LINE[recombinate_line]
                    if current_line[-1] not in "+*" and eval(current_line) ==0:
                        max_len = max(max_len,len(current_line))
print(max_len)
#126
