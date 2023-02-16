# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def random_list (len, min, max):
    list=[]
    for i in range (len):
        list.append(random.randint(min,max))
    return list

N=int(input("Введите колличество элементов в списке: "))
min=int(input("Введите минимальное значение списка: "))
max=int(input("Введите максимальное значение списка: "))
minimum=int(input("Введите минимальное значение элемента: "))
maximum=int(input("Введите максимальное значение элемента: "))

list_1=random_list (N, min, max)
print(list_1) 
for i in range(len(list_1)):
    if minimum<list_1[i]<maximum:
        print(f"{i} " ,  end="")