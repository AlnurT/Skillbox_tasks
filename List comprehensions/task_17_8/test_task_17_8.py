import pytest
from task_17_8.task_17_8 import knock_down_sticks


@pytest.mark.parametrize(
    ("left_i", "right_i", "sticks_after_game"),
    [(1, 3, "...||"), (3, 5, "||..."), (2, 4, "|...|")],
)
def test_knock_down_sticks(left_i, right_i, sticks_after_game):
    assert knock_down_sticks("|" * 5, left_i, right_i) == sticks_after_game
