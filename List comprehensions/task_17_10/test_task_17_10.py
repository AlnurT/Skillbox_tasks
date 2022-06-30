import string

import pytest
from task_17_10.task_17_10 import encrypt_text


@pytest.mark.parametrize(
    ("text", "shift", "cypher"),
    [
        ("abc xyz!", 0, "abc xyz!"),
        ("abc xyz!", 1, "bcd yza!"),
        ("abc xyz!", -1, "zab wxy!"),
        ("abc xyz!", 26, "abc xyz!"),
        ("abc xyz!", -26, "abc xyz!"),
    ],
)
def test_encrypt_text(text, shift, cypher):
    assert encrypt_text(text, shift, string.ascii_lowercase) == cypher
