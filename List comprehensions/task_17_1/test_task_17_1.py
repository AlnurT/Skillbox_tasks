import pytest
from task_17_1.task_17_1 import search_for_vowels

vowels = frozenset("абеёиоуыэюя")


@pytest.mark.parametrize(
    ("text", "list_of_vowels"),
    [
        ("ВАй ты!", ["а", "ы"]),
        ("Вй т!", []),
        ("", []),
    ],
)
def test_vowels_is_in_the_text(text, list_of_vowels):
    assert search_for_vowels(vowels, text) == list_of_vowels
