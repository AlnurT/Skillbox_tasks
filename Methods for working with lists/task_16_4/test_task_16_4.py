import pytest
from task_16_4.task_16_4 import is_action_in_guests_list


@pytest.mark.parametrize(
    ("guests_num", "action", "is_action"),
    [
        (0, "пришёл", True),
        (6, "пришёл", False),
        (6, "ушёл", True),
        (0, "ушёл", False),
        (0, "пора спать", False),
    ],
)
def test_add_or_remove_guests(guests_num, action, is_action):
    assert is_action_in_guests_list(guests_num, action) == is_action
