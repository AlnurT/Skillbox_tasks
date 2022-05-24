from task_17_3.task_17_3 import create_list_of_thehighest_scores


def test_create_list_of_thehighest_scores():
    assert create_list_of_thehighest_scores([5.09, 6.56, 9.99], [5.08, 7.57, 9.99]) == [
        5.09,
        7.57,
        9.99,
    ]
