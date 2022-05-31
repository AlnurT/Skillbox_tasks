import pytest
from task_18_7.task_18_7 import check_correct_ip_input


@pytest.mark.parametrize(
    ("ip_address", "error"),
    [("128.16.35", 1), ("128.16.35.a4", 2), ("128.16.35.256", 3), ("128.0.0.255", 0)],
)
def test_check_correct_ip_input(ip_address, error):
    assert check_correct_ip_input(ip_address) == error
