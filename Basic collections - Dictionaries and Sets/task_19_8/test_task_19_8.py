import pytest
from task_19_8.task_19_8 import is_number_in_possible_numbers


@pytest.mark.parametrize(
    ("possible_numbers", "answer"),
    [({1, 2, 3, 5}, "Да"), ({1, 2, 5}, "Нет"), ({5}, "Нет")],
)
def test_is_number_in_possible_numbers(possible_numbers, answer):
    assert is_number_in_possible_numbers({1, 2, 3, 4}, possible_numbers, 3) == answer
