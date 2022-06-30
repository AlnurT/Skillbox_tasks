import pytest
from task_16_4.task_16_4 import adding_or_removing_guest, is_action_in_guests_list


@pytest.mark.parametrize(
    ("guests_num", "action", "is_action"),
    [
        (0, "in", True),
        (6, "in", False),
        (6, "out", True),
        (0, "out", False),
        (0, "time to sleep", False),
    ],
)
def test_is_action_in_guests_list(guests_num, action, is_action):
    assert is_action_in_guests_list(guests_num, action) == is_action


@pytest.mark.parametrize(
    ("guests_list", "guest_name", "in_or_out", "new_guests_list"),
    [
        ([], "Talgat", "in", ["Talgat"]),
        (["Talgat"], "Talgat", "out", []),
    ],
)
def test_adding_or_removing_guest(guests_list, guest_name, in_or_out, new_guests_list):
    assert (
        adding_or_removing_guest(guests_list, guest_name, in_or_out) == new_guests_list
    )
