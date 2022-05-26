import pytest
from task_16_4.task_16_4 import add_or_remove_guests

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя", "Талга"]


@pytest.mark.parametrize(
    ("guests_before_action", "action", "guests_after_action"),
    [
        ([], "пришёл", (-1, ["Талга"])),
        (guests, "пришёл", (6, guests)),
        (["Талга"], "ушёл", (-1, [])),
        ([], "ушёл", (0, [])),
    ],
)
def test_add_or_remove_guests(guests_before_action, action, guests_after_action):
    assert (
        add_or_remove_guests(guests_before_action, action, "Талга")
        == guests_after_action
    )
