'''(№ 7401) (П. Тюрин) У исполнителя имеются две команды, которые обозначены номерами:

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


alll = set()

def F(start=2,end=70,history=[],plus=False):
    alll.add(start)
    history2 = list(history)
    history2.append(start)

    if start == end and ((16 in history and 8 in history) or 32 in history):
        return 1
    if start == end:
        return 0
    if start > end:
        return 0

    if not(plus):
        return F(start*2,end,history2,plus= False) + F(start+3,end,history2,plus = True)
    else:
        return F(start * 2, end, history2, plus=False)


F()
print(len(alll))
#69
#Не вижу ошибку