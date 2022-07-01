import pytest
from task_18_8.task_18_8 import check_shift_of_string


@pytest.mark.parametrize(
    ("some_string", "shift"),
    [("abcde", 0), ("bcdea", 1), ("cdeab", 2), ("edcba", -1)],
)
def test_check_shift_of_string(some_string, shift):
    assert check_shift_of_string("abcde", some_string) == shift
