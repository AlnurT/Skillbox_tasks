from task_17_9.task_17_9 import expand_list


def test_expand_list():
    assert expand_list([[[1], [2]], [[3], [4]]]) == [1, 2, 3, 4]
