import pytest
from task_18_2.task_18_2 import find_long_word


@pytest.mark.parametrize(
    ("text", "long_word"),
    [("Я есть длинная строка", "длинная"), ("Я о", "Я"), ("Я", "Я")],
)
def test_find_long_word(text, long_word):
    assert find_long_word(text) == long_word
