"""Задача 10. Шифр Цезаря

Юлий Цезарь использовал свой способ шифрования текста.
Каждая буква заменялась на следующую по алфавиту через K позиций по кругу.
Если взять русский алфавит и K = 3, то в слове, которое мы хотим зашифровать,
буква А станет буквой Г, Б станет Д и так далее.

Пользователь вводит сообщение, а также значение сдвига.
Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.

Пример:
Введите сообщение: это питон.
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср.
"""


def create_alphabet():
    alphabet = ""
    for unicode in range(ord("а"), ord("я") + 1):
        alphabet += chr(unicode)
    return alphabet


def encrypt_text(text: str, shift: int, alphabet: str) -> str:
    cypher = ""
    for symbol in text:
        num_symbol = alphabet.find(symbol)
        if (num_symbol + shift) >= 31 and num_symbol != -1:
            cypher += alphabet[num_symbol + shift - len(alphabet)]
        elif num_symbol != -1:
            cypher += alphabet[num_symbol + shift]
        else:
            cypher += symbol
    return cypher


def main():
    text = input("Введите сообщение: ").lower()
    shift = int(input("Введите сдвиг: "))

    print(f"Зашифрованное сообщение: {encrypt_text(text, shift, create_alphabet())}")


if __name__ == "__main__":
    main()
