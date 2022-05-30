"""Задача 5. Разворот

На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
Реализуйте код, который разворачивает последовательность символов,
заключённую между первым и последним появлением буквы h, в противоположном порядке.

Пример 1:

Введите строку: hqwehrty
Развёрнутая последовательность между первым и последним h: ewq

Пример 2:

Введите строку: hh
Развёрнутая последовательность между первым и последним h:

Пример 3:

Введите строку: hhqwerh
Развёрнутая последовательность между первым и последним h: rewqh
"""


def reverse_string_between_first_and_last_symbol(
    random_string: str, symbol: str
) -> str:
    left_border = random_string.index(symbol)
    right_border = random_string.rindex(symbol) - 1
    return random_string[right_border:left_border:-1]


def main():
    random_string = input("Введите строку: ")
    symbol = input("Введите повторяющийся символ: ")
    new_string = reverse_string_between_first_and_last_symbol(random_string, symbol)

    print(
        f"Развёрнутая последовательность между первым и последним {symbol}: {new_string}"
    )


if __name__ == "__main__":
    main()
