'''(№ 7401) (П. Тюрин) У исполнителя имеются две команды,
 которые обозначены номерами:

1. Умножить на 2
2. Прибавить 3

Первая команда умножает число на 2, вторая увеличивает его на 3.
Программа для исполнителя – это последовательность команд.
 Рассматриваются все программы, в которых при исходном числе
2 результатом является число 70, причём
а) команда сложения не применяется более двух раз подряд;
б) траектория вычислений проходит либо через числа 8 и 16,
либо через число 32 (но не через все три числа одновременно).
Сколько различных чисел содержится во всех таких траекториях вычислений? '''


alll = list()

def F(start=2,end=70,history=[],plus=0):

    history2 = list(history)
    history2.append(start)

    if start == end and ((16 in history and 8 in history) or 32 in history):
        if not( 16 in history and 8 in history and 32 in history ):
            alll.extend(history2)
            return 1
    if start == end:
        return 0
    if start > end:
        return 0

    if  plus !=2:
        return F(start*2,end,history2,plus= 0) + F(start+3,end,history2,plus = plus+1)
    else:
        return F(start * 2, end, history2, plus=0)


F()
print(len(set(alll)))
#12
