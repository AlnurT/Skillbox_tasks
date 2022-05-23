from task_16_6.task_16_6 import find_unique_numbers


def test_find_unique_numbers():
    assert find_unique_numbers([8, 2, 5], [8, 4, 5]) == {8, 2, 5, 4}
