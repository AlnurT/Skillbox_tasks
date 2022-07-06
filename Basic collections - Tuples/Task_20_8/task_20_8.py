"""Задача 8. Контакты 3

Мы уже помогали Степану с реализацией телефонной книги на телефоне, однако внезапно оказалось,
что книге не хватает ещё одной полезной функции: поиска.

Напишите программу, которая бесконечно запрашивает у пользователя действие,
которое он хочет совершить: добавить контакт или найти человека в списке контактов по фамилии.

Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона,
добавляет их в словарь и выводит на экран текущий словарь контактов.
Если этот человек уже есть в словаре, то выводится соответствующее сообщение.

Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией и их номера телефонов.
Поиск не должен зависеть от регистра символов.

Пример работы программы:
Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1

Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
Введите номер телефона: 888
Текущий словарь контактов: {('Иван', 'Сидоров'): 888}

Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1

Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
Такой человек уже есть в контактах.
Текущий словарь контактов: {('Иван', 'Сидоров'): 888}

Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1

Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
Введите номер телефона: 999
Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}

Введите номер действия:
 1. Добавить контакт
 2. Найти человека
2

Введите фамилию для поиска: Сидоров
Иван Сидоров 888

Введите номер действия:
 1. Добавить контакт
 2. Найти человека
…….
"""


def add_contact(telephone_book: dict, person: tuple, telephone_number: int) -> dict:
    if person in telephone_book.keys():
        print("Such a person is already in the contacts.")
    else:
        telephone_book[person] = telephone_number
        print(f"Current contact dictionary: {telephone_book}\n")
    return telephone_book


def search_contact(telephone_book: dict, person_surname: str) -> dict:
    found_contacts = {}
    for person in telephone_book.keys():
        if person[1] == person_surname:
            found_contacts[person] = telephone_book[person]
            print(" ".join(person), found_contacts[person])
    return found_contacts


def main():
    action = 0
    telephone_book = {}
    while action != 3:
        action = int(
            input(
                "Enter action number:\n"
                "1) Add contact\n"
                "2) Find a person\n"
                "3) Exit\n"
            )
        )

        if action == 1:
            person = tuple(
                input(
                    "Enter name and surname of new contact (through a space): "
                ).split()
            )
            telephone_number = int(input("Enter telephone number: "))
            add_contact(telephone_book, person, telephone_number)
        elif action == 2:
            person_surname = input("Enter surname for searching: ")
            search_contact(telephone_book, person_surname)


if __name__ == "__main__":
    main()
