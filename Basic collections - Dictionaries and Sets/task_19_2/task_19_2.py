"""Задача 2. География

Антон, помимо программирования, также увлекается и географией, поэтому он решил связать эти две области и
написать для своего проекта небольшую программу-навигатор.

Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся,
в одну строку. После пользователь вводит три названия городов.
Реализуйте такую программу и для каждого из трёх городов укажите, в какой стране он находится.
Если такого города нет, то выведите соответствующее сообщение.

Пример:
Количество стран: 2
Первая страна: Россия Москва Петербург Новгород
Вторая страна: Германия Берлин Лейпциг Мюнхен

Первый город: Москва
Город Москва расположен в стране Россия.

Второй город: Мюнхен
Город Мюнхен расположен в стране Германия.

Третий город: Рим
По городу Рим данных нет.
"""


def create_dict_of_counry(country_dict: dict, country: list) -> dict:
    country_dict[country[0]] = set(country[1:])
    return country_dict


def search_coutry_for_city_in_dict(country_dict: dict, city: str) -> str:
    for country in country_dict:
        if city in country_dict[country]:
            return country
    return ""


def main():
    country_num = int(input("Кол-во стран: "))
    country_dict = {}
    for num in range(1, country_num + 1):
        country = input(f"{num} страна: ").split()
        country_dict = create_dict_of_counry(country_dict, country)

    for num in range(1, 4):
        city = input(f"\n{num} город: ")
        country = search_coutry_for_city_in_dict(country_dict, city)
        if country == "":
            print(f"По городу {city} данных нет.")
        else:
            print(f"Город {city} расположен в стране {country}.")


if __name__ == "__main__":
    main()
