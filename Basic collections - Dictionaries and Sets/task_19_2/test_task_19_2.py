import pytest
from task_19_2.task_19_2 import create_dict_of_counry, search_coutry_for_city_in_dict

country_dict = {
    "Россия": {"Москва", "Петербург", "Новгород"},
    "Германия": {"Берлин", "Лейпциг", "Мюнхен"},
}


def test_create_dict_of_counry():
    assert create_dict_of_counry(
        country_dict, ["Казахстан", "Алматы", "Астана", "Рудный"]
    ) == {
        "Россия": {"Москва", "Петербург", "Новгород"},
        "Германия": {"Берлин", "Лейпциг", "Мюнхен"},
        "Казахстан": {"Алматы", "Астана", "Рудный"},
    }


@pytest.mark.parametrize(
    ("city", "country"),
    [
        ("Лейпциг", "Германия"),
        ("Москва", "Россия"),
        ("Сидней", ""),
    ],
)
def test_search_coutry_for_city_in_dict(city, country):
    assert search_coutry_for_city_in_dict(country_dict, city) == country
