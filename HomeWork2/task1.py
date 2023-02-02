# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример: 5 -> 1 0 1 1 0

n=int(input("Введите количество монеток, лежащих на столе: "))
tails = 0
eagle = 0
print("Укажите сторону монеты. Где 0 - это решка, а 1 - орел")
for i in range(n):
    coin = int(input(f'{i+1}-я монета: '))
    if coin == 0:
        tails += 1
    else: 
        eagle += 1
if tails>=eagle:
    print(eagle)
else: print(tails)    