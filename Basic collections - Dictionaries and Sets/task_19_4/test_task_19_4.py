from task_19_4.task_19_4 import calculate_the_quantity_and_cost_of_goods

store = {
    "1": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}


def test_calculate_the_quantity_and_cost_of_goods():
    assert calculate_the_quantity_and_cost_of_goods(store, "1") == (105, 10311)
