"""Задача 6. Сжатие

С увеличением объёма данных возникла потребность в сжатии этих данных без потери важной информации.
Для этого было придумано кодирование, которое осуществляется следующим образом:

s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ и
количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку,
кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран.
Кодирование должно учитывать регистр символов.

Пример:
Введите строку: aaAAbbсaaaA

Закодированная строка: a2A2b2с1a3A1
"""


def encode_string(text: str) -> str:
    encode_text = ""
    repeat = 1
    for num in range(len(text) - 1):
        if text[num] == text[num + 1]:
            repeat += 1
        elif num == len(text) - 2:
            encode_text = "{}{}{}{}1".format(
                encode_text, text[num], repeat, text[num + 1]
            )
        else:
            encode_text = "{}{}{}".format(encode_text, text[num], repeat)
            repeat = 1
    return encode_text


def main():
    text = input("Введите строку: ")

    encode_text = encode_string(text)
    print(f"Закодированная строка: {encode_text:s}")


if __name__ == "__main__":
    main()
