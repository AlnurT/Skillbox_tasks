"""Задача 7. Пицца

В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них в определённый период.
Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.

На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида
«Покупатель — название пиццы — количество заказанных пицц».
Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
Учитывайте, что один человек может заказать одно и то же несколько раз.

Пример:
Введите количество заказов: 6
Первый заказ: Иванов Пепперони 1
Второй заказ: Петров Де-Люкс 2
Третий заказ: Иванов Мясная 3
Четвёртый заказ: Иванов Мексиканская 2
Пятый заказ: Иванов Пепперони 2
Шестой заказ: Петров Интересная 5

Иванов:
    Мексиканская: 2
    Мясная: 3
    Пепперони: 3

Петров:
    Де-Люкс: 2
    Интересная: 5
"""


def add_order_in_dict(orders_dict: dict, order: list) -> dict:
    name = order[0]
    orders_dict[name] = orders_dict.get(name, {})
    pizza = order[1]
    pizza_num = orders_dict[name].get(pizza, 0) + int(order[2])
    orders_dict[name][pizza] = pizza_num
    return orders_dict


def main():
    orders_num = int(input("Введите количество заказов: "))
    orders_dict = {}
    for num in range(1, orders_num + 1):
        order = input(f"{num} заказ: ").split()
        orders_dict = add_order_in_dict(orders_dict, order)

    for name in orders_dict:
        print(f"\n{name}:")
        for pizza, pizza_num in orders_dict[name].items():
            print(f"\t{pizza}: {pizza_num}")


if __name__ == "__main__":
    main()
