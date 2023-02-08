# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
def random_list (len, min, max):
    list=[]
    for i in range (len):
        list.append(random.randint(min,max))
    return list

N=int(input("Введите колличество элементов в массиве: "))
min=1
max=int(input("Введите максимальное значение списка: "))
X=int(input("Введите заданное число: "))
A=random_list (N, min, max)
print(A) 
A.sort()
Mn=A[0]
Mx=A[-1]
for i in range(len(A)):
    if Mn==X:
        Mn=A[1]
    elif Mx==X:
        Mx=A[-2]    
    elif A[i]<X and A[i]>=Mn:
       Mn=A[i]
    elif A[i]>X and A[i]<Mx:
       Mx=A[i]
if  X-Mn>=Mx-X:
    print(Mx)
else: print(Mn)  