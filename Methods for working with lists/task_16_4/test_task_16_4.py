"""import pytest
from task16_4.task16_4 import add_or_remove_guests

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя", "Талга"]


@pytest.mark.parametrize(
    ("guests_before_action", "action", "guests_after_action"),
    [
        ([], "пришёл", ["Талга"]),
        (guests, "пришёл", guests),
        (["Талга"], "ушёл", []),
        ([], "ушёл", []),
    ],
)
def test_add_or_remove_guests(guests_before_action, action, guests_after_action):
    assert (
        add_or_remove_guests(guests_before_action, action, "Талга")
        == guests_after_action
    )"""
