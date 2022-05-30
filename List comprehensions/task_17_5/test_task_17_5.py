import pytest
from task_17_5.task_17_5 import reverse_string_between_first_and_last_symbol


@pytest.mark.parametrize(
    ("random_string", "new_string"),
    [
        ("hqwehrty", "ewq"),
        ("hh", ""),
        ("hhqwerh", "rewqh"),
    ],
)
def test_reverse_string_between_first_and_last_symbol(random_string, new_string):
    assert (
        reverse_string_between_first_and_last_symbol(random_string, "h") == new_string
    )
