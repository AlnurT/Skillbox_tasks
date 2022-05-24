import pytest
from task_19_10.task_19_10 import is_palindrome


@pytest.mark.parametrize(
    ("text", "result"),
    [
        ("a", True),
        ("ab", False),
        ("aa", True),
        ("aab", True),
        ("abc", False),
        ("aabc", False),
        ("aabbc", True),
    ],
)
def test_is_palindrome(text, result):
    assert is_palindrome(text) == result
