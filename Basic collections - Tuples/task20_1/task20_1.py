"""Задача 2. Универсальная программа 2

Спустя некоторое время заказчик попросил вас немного изменить скрипт для криптографии:
теперь индексы элементов должны быть простыми числами.
Напишите функцию, которая возвращает список элементов итерируемого объекта (кортежа, строки, списка, словаря),
у которых индекс — это простое число. Для проверки на простое число напишите отдельную функцию is_prime.
Основной код оставьте пустым (используйте его только для тестирования).

Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return и так же возвращала список.

Пример вызова функции:
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
Ответ в консоли: [2, 3, 5, 7]

Пример вызова функции:
print(crypto('О Дивный Новый мир!'))
Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']
"""


def is_prime(index: int) -> bool:
    if index % 2 == 0 and index != 2 or index == 1:
        return False
    divisor = 3
    while index % divisor != 0 and divisor ** 2 < index:
        divisor += 2
    return divisor ** 2 > index


def create_list_with_prime_index(obj) -> list:
    if type(obj) is dict:
        return [obj[key] for index, key in enumerate(obj) if is_prime(index)]
    else:
        return [element for index, element in enumerate(obj) if is_prime(index)]


def main():
    print(f"Список: {create_list_with_prime_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
    print(f"Кортеж: {create_list_with_prime_index((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))}")
    print(f"Строка: {create_list_with_prime_index('О Дивный Новый мир!')}")
    print(
        f"Словарь: {create_list_with_prime_index({'a': 1, 'b': 10, 'c': 100, 'd': 1000, 'e': 10000, 'f': 100000})}"
    )


if __name__ == "__main__":
    main()
