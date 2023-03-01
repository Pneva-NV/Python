# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1. Добавить контакт
# 2. Просмотр справочника
# 3. Поиск данных
# 4. Изменение данных
# 5. Удаление данных

import os
file= "c:/Users/apnio/Git/Семинар_Python/HomeWork8/Телефонная книга.txt"

def append_contact(file):
    contact=input("Введите новый контакт ФИО и телефон: ")
    with open(file, "a", encoding="UTF-8") as f:
        f.write (f"\n{contact}" )
        print("Контакт добавлен")

def read_contact(file):
    with open(file, "r", encoding="UTF-8") as f:
        print(f.read ())

def search_contact(file):
    search=input("Введите данные для поиска в каталоге: ")
    with open(file, "r", encoding="UTF-8") as f:
        for line in f:
            if search in line:
                print(line)

def change_contact(file, info_1,  info_2):
    info_old = input (info_1)
    info_new = input (info_2)
    with open(file, "r", encoding="UTF-8") as f:
        box=f.read()
    with open(file, "w", encoding="UTF-8") as f:
        box=box.replace(info_old, info_new)
        f.write(box)
        print("Данные изменены")

def remove_contact(file, info):
    remove = input (info)
    with open(file, "r", encoding="UTF-8") as f:
        box=f.readlines()
    with open(file, "w", encoding="UTF-8") as f:
        for line in box:
            if remove not in line.strip("\n"):
                f.write(line)
        print("Данные удалены")
                    
def console(file):
    print("Для выполнения операций со справочником выполнить следующие действия: \n"
          "1 - Добавление нового контакта \n"
          "2 - Выгрузка данных из справочника \n"
          "3 - Поиск данных \n"
          "4 - Изменение данных\n"
          "5 - Удаление данных\n"
          "0 - Выход")
    while (enter:=int(input("Введите нужную цифру: "))) !=0:
        if enter == 1: append_contact(file)
        elif enter == 2: read_contact(file)
        elif enter == 3: search_contact(file)
        elif enter == 4: change_contact(file, "Введите данные, которые нужно изменить: ", "Введите новые данные: ")
        elif enter == 5: remove_contact(file, "Введите данные, которые нужно удалить: ")
        else: print("Некорректный ввод")
        
console(file)