import pytest
from task_19_7.task_19_7 import add_order_in_dict

order = ["Иванов", "Пепперони", "1"]


@pytest.mark.parametrize(
    ("orders_dict", "new_orders_dict"),
    [
        ({}, {"Иванов": {"Пепперони": 1}}),
        ({"Иванов": {"Пепперони": 2}}, {"Иванов": {"Пепперони": 3}}),
    ],
)
def test_add_order_in_dict(orders_dict, new_orders_dict):
    assert add_order_in_dict(orders_dict, order) == new_orders_dict
