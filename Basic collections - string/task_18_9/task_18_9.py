"""Задача 9. Сообщение

Вашему другу надоело общаться простыми сообщениями, и он решил делать это необычным способом:
он переворачивает каждое слово в тексте, при этом не трогая знаки препинания.

Пользователь вводит текст, состоящий из слов и знаков препинания. Напишите программу,
которая переворачивает (записывает в обратном порядке) все слова текста, оставив знаки препинания без изменений.
Словом в тексте считается последовательность символов из прописных и строчных букв кириллицы.

Пример 1:
Сообщение: Это задание очень! простое.
Новое сообщение: отЭ еинадаз ьнечо! еотсорп.

Пример 2:
Сообщение: Хотя ,. возм:ожно и нет.
Новое сообщение: ятоХ ,. мзов:онжо и тен.
"""

from re import split


def flip_message(message: str) -> str:
    message_list = split(r"(\W+)", message)
    return "".join([text[::-1] if text.isalpha() else text for text in message_list])


def main():
    message = input("Сообщение: ")

    new_message = flip_message(message)
    print(f"Новое сообщение: {new_message}")


if __name__ == "__main__":
    main()
