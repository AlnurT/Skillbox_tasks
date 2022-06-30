"""Задача 4. Вечеринка

В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения,
а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите».
В ходе вечеринки люди приходили и уходили, ночевать остались не все.
К тому же и сама дача не резиновая — на ней помещается всего шесть человек.

Дан изначальный список гостей — имена тех, кто пришёл к началу:
guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]

Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость,
и исходя из ответа добавляет в список или удаляет из него нужное имя.
При этом гостей может быть не больше шести. Имена запрашиваются до тех пор,
пока пользователь не введёт сообщение «Пора спать».
Пример:

Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
Гость пришёл или ушёл? пришёл
Имя гостя: Алекс
Привет, Алекс!

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? пришёл
Имя гостя: Гоша
Прости, Гоша, но мест нет.

Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
Гость пришёл или ушёл? ушёл
Имя гостя: Ваня
Пока, Ваня!

Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’,  ‘Алекс’]
Гость пришёл или ушёл? Пора спать

Вечеринка закончилась, все легли спать.
"""


dict_of_messages = {
    ("in", False): "прости, но мест нет.",
    ("in", True): "привет!",
    ("out", False): "такого человека нет. Гостей больше нет",
    ("out", True): "пока.",
    ("time to sleep", False): "прости, но вечеринка закончилась, все легли спать.",
}


def is_action_in_guests_list(guests_num: int, entrance_or_exit: str) -> bool:
    return not (
        entrance_or_exit == "time to sleep"
        or (guests_num == 0 and entrance_or_exit == "out")
        or (guests_num == 6 and entrance_or_exit == "in")
    )


def adding_or_removing_guest(guests: list, guest_name: str, in_or_out: str) -> list:
    if in_or_out == "in":
        guests.append(guest_name)
    elif in_or_out == "out":
        guests.remove(guest_name)
    return guests


def main():
    guests = ["Alnur", "Ivan", "Alexey", "Lisa", "Ira"]
    in_or_out = ""
    while in_or_out != "time to sleep":
        print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
        in_or_out = input("Гость пришёл(in) или ушёл(out)? ")
        guest_name = input("Имя гостя: ")

        action = is_action_in_guests_list(len(guests), in_or_out)
        if action:
            adding_or_removing_guest(guests, guest_name, in_or_out)

        print(f"\n{guest_name}, {dict_of_messages[in_or_out, action]}")


if __name__ == "__main__":
    main()