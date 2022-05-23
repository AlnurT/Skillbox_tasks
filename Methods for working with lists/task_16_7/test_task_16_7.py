import pytest
from task_16_7.task_16_7 import check_the_size_of_skates_per_person

skate_sizes = {41: 2, 42: 0, 43: 1}


@pytest.mark.parametrize(("human_size", "for_sale"), [(42, 1), (42, 0), (44, 0)])
def test_check_the_size_of_skates_per_person(human_size, for_sale):
    assert check_the_size_of_skates_per_person(skate_sizes, human_size) == for_sale
