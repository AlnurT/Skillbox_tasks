import pytest
from task_18_5.task_18_5 import check_password


@pytest.mark.parametrize(
    ("password", "error"),
    [
        ("qwerty", 1),
        ("qwertyui", 2),
        ("qWerty12", 3),
        ("qWerty123", 0),
    ],
)
def test_check_password(password, error):
    assert check_password(password) == error
