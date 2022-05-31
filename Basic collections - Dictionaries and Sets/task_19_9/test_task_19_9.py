import pytest
from task_19_9.task_19_9 import change_family_member_level


@pytest.mark.parametrize(
    ("family_member_level_dict", "relatives", "result"),
    [
        ({}, ["Alexei", "Peter_I"], {"Peter_I": 0, "Alexei": 1}),
        (
            {"Peter_I": 0, "Alexei": 1},
            ["Peter_II", "Alexei"],
            {"Peter_I": 0, "Alexei": 1, "Peter_II": 2},
        ),
    ],
)
def test_change_family_member_level(family_member_level_dict, relatives, result):
    assert change_family_member_level(family_member_level_dict, relatives) == result
