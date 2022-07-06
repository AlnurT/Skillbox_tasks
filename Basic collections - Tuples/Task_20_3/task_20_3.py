"""Задача 3. Функция

Напишите функцию, которая на вход принимает кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.

Если элемента нет вовсе — вернуть пустой кортеж.
Если элемент встречается только один раз — вернуть кортеж, который начинается с этого элемента и идёт до конца исходного.

Пример вызова функции:
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)
"""


def slicer(numbers_tuple: tuple, random_number: int) -> tuple:
    number_count = numbers_tuple.count(random_number)
    start = (
        numbers_tuple.index(random_number) if number_count >= 1 else len(numbers_tuple)
    )
    end = (
        numbers_tuple.index(random_number, start + 1) + 1
        if number_count >= 2
        else len(numbers_tuple)
    )
    return numbers_tuple[start:end]


def main():
    numbers_tuple = tuple(map(int, input("Numbers for tuple: ").split()))
    random_number = int(input("Enter a random number: "))

    print(f"Sliced tuple: {slicer(numbers_tuple, random_number)}")


if __name__ == "__main__":
    main()
