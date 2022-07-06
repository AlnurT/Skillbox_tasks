"""Задача 7. Ролики

Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики любого размера,
которые не меньше размера его ноги.

Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.

Пример:
Кол-во коньков: 4
Размер 1 пары: 41
Размер 2 пары: 40
Размер 3 пары: 39
Размер 4 пары: 42

Кол-во людей: 3
Размер ноги 1 человека: 42
Размер ноги 2 человека: 41
Размер ноги 3 человека: 42

Наибольшее кол-во людей, которые могут взять ролики: 2
"""


def check_the_size_of_skates_per_person(skate_sizes: dict, human_size: int) -> int:
    for size in skate_sizes:
        if human_size <= size and skate_sizes[size] > 0:
            skate_sizes[size] -= 1
            return 1
    return 0


def main():
    num_of_skates = int(input("Кол-во коньков: "))
    skate_sizes = {}
    suitable_skates = 0

    for skates in range(num_of_skates):
        print(f"Размер {skates + 1} пары:", end=" ")
        size = int(input())
        skate_sizes[size] = skate_sizes.get(size, 0) + 1
    skate_sizes = dict(sorted(skate_sizes.items(), key=lambda x: x[0]))

    num_of_human = int(input("\nКол-во людей: "))
    for human in range(num_of_human):
        print(f"Размер ноги {human + 1} человека:", end=" ")
        human_size = int(input())
        suitable_skates += check_the_size_of_skates_per_person(skate_sizes, human_size)

    print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {suitable_skates}")


if __name__ == "__main__":
    main()
