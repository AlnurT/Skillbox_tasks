"""Задача 7. Двумерный список

Как мы говорили ранее, в программировании часто приходится писать код исходя из результата, который требует заказчик.
В этот раз заказчику нужно получить вот такой двумерный список:

[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.
"""


def generate_sublists_in_list(total_numbers: int, num_sublist: int) -> list:
    first_list = list(range(1, total_numbers + 1))
    return [first_list[numb::num_sublist] for numb in range(num_sublist)]


def main():
    total_numbers = int(input("Общее кол-во элементов: "))
    num_sublists = int(input("Кол-во подсписков: "))

    print(f"Список: {generate_sublists_in_list(total_numbers, num_sublists)}")


if __name__ == "__main__":
    main()
