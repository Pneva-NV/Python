# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

M = int(input("Введите 1-й элемент: "))
k = int(input("Введите увеличивающий коэф.: "))
N = int(input("Введите количество элементов: "))

list_1=[M]

for i in range(1, N):
    if N==0:
        print("Нет элементов")
    elif N>1:
        box=M+k
        M+=k
        list_1.append(box)
print(list_1)