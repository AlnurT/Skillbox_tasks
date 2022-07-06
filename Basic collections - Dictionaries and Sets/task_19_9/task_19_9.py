"""Задача 9. Родословная

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждому элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента высота на один больше, чем у его родителя.
Вам нужно написать программу, которая по заданному генеалогическому древу определяет высоту всех его элементов.

Программа получает на вход N количество человек в генеалогическом древе. Далее следует N − 1 строк,
в каждой из которых задаётся родитель для каждого элемента дерева, кроме родоначальника.
Каждая строка имеет вид «имя_потомка имя_родителя».

Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту).
После вывода имени каждого элемента необходимо вывести его высоту.

Пример:
Введите количество человек: 9

Первая пара: Alexei Peter_I
Вторая пара: Anna Peter_I
Третья пара: Elizabeth Peter_I
Четвёртая пара: Peter_II Alexei
Пятая пара: Peter_III Anna
Шестая пара: Paul_I Peter_III
Седьмая пара: Alexander_I Paul_I
Восьмая пара: Nicholaus_I Paul_I

«Высота» каждого члена семьи:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2
"""


def change_family_member_level(family_member_level_dict: dict, relatives: list) -> dict:
    if relatives[1] not in family_member_level_dict:
        family_member_level_dict[relatives[1]] = 0
    family_member_level_dict[relatives[0]] = family_member_level_dict[relatives[1]] + 1
    return family_member_level_dict


def main():
    people_number = int(input("Введите количество человек: "))
    family_member_level_dict = {}

    for pair in range(1, people_number):
        relatives = input(f"{pair} пара: ").split()
        change_family_member_level(family_member_level_dict, relatives)

    print("\n«Высота» каждого члена семьи:")
    for family_member in sorted(family_member_level_dict.keys()):
        print(family_member, family_member_level_dict[family_member])


if __name__ == "__main__":
    main()
