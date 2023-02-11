# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
def random_list (len, min, max):
    list=[]
    for i in range (len):
        list.append(random.randint(min,max))
    return list

n=int(input("Введите колличество элементов в 1-м числовом наборе: "))
m=int(input("Введите колличество элементов во 2-м числовом наборе: "))
min=1
max=10
A_list=random_list (n, min, max)
B_list=random_list (m, min, max)
print(A_list)
print(B_list)
A_set=set(A_list)
B_set=set(B_list)
print(A_set.intersection(B_set))