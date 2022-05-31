"""Задача 10. Снова палиндром

Пользователь вводит строку. Необходимо написать программу, которая определяет,
существует ли у этой строки такая перестановка, при которой она станет палиндромом.
Выведите соответствующее сообщение.

Пример 1:
Введите строку: aab
Можно сделать палиндромом

Пример 2:
Введите строку: aabc
Нельзя сделать палиндромом
"""


def is_palindrome(text: str) -> bool:
    text_dict = {symbol: text.count(symbol) for symbol in set(text)}
    odd_count = 0
    for symbol_count in text_dict.values():
        if symbol_count % 2 != 0:
            odd_count += 1
        if odd_count == 2:
            return False
    return True


def main():
    text = input("Введите строку: ")

    if is_palindrome(text):
        print("Можно сделать палиндромом")
    else:
        print("Нельзя сделать палиндромом")


if __name__ == "__main__":
    main()
