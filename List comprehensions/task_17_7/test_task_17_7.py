from task_17_7.task_17_7 import generate_sublists_in_list


def test_generate_list():
    assert generate_sublists_in_list(5, 3) == [[1, 4], [2, 5], [3]]


def test_generate_list_if_sublists_more_then_numbers():
    assert generate_sublists_in_list(2, 3) == [[1], [2], []]
