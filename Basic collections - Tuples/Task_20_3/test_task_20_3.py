import pytest
from Task_20_3.task_20_3 import slicer


@pytest.mark.parametrize(
    ("numbers_tuple", "random_number", "sliced_tuple"),
    [
        ((1, 2, 3, 4, 2, 5), 2, (2, 3, 4, 2)),
        ((1, 2, 3, 4, 3, 5), 2, (2, 3, 4, 3, 5)),
        ((1, 3, 3, 4, 3, 5), 2, ()),
    ],
)
def test_slicer(numbers_tuple, random_number, sliced_tuple):
    assert slicer(numbers_tuple, random_number) == sliced_tuple
