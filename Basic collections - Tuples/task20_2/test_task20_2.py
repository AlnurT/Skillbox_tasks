import pytest
from task20_2.task20_2 import create_list_with_prime_index, is_prime


@pytest.mark.parametrize(
    ("index", "result"),
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (8, False),
        (11, True),
    ],
)
def test_is_prime(index, result):
    assert is_prime(index) == result


@pytest.mark.parametrize(
    ("obj", "prime_list"),
    [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 5, 7]),
        ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), [2, 3, 5, 7]),
        ("О Дивный Новый мир!", ["Д", "и", "н", "й", "в", "й", "р"]),
        (
            {"a": 1, "b": 10, "c": 100, "d": 1000, "e": 10000, "f": 100000},
            [100, 1000, 100000],
        ),
    ],
)
def test_create_list_with_prime_index(obj, prime_list):
    assert create_list_with_prime_index(obj) == prime_list
