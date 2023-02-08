# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
def random_list (len, min, max):
    list=[]
    for i in range (len):
        list.append(random.randint(min,max))
    return list

N=int(input("Введите колличество элементов в массиве: "))
min=1
max=int(input("Введите максимальное значение списка: "))
X=int(input("Введите искомое число: "))
A=random_list (N, min, max)
print(A)
box=0
for i in range(len(A)):
    if A[i]==X:
        box+=1
print(f"Искомое число встречается в массиве {box} раз.")    