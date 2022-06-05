import pytest
from Task_20_9.task_20_9 import create_dict_of_results, search_for_winners


@pytest.mark.parametrize(
    ("old_results_dict", "result", "entry", "new_results_dict"),
    [
        ({}, ["55", "Alnur"], 3, {"Alnur": (55, 3)}),
        ({"Alnur": (55, 3)}, ["66", "Alnur"], 4, {"Alnur": (66, 4)}),
    ],
)
def test_create_dict_of_results(old_results_dict, result, entry, new_results_dict):
    assert create_dict_of_results(old_results_dict, result, entry) == new_results_dict


@pytest.mark.parametrize(
    ("results_dict", "winner"),
    [
        ({"Alnur": (66, 3), "Talgat": (77, 4)}, ("Talgat", 77)),
        ({"Alnur": (66, 3), "Igor": (66, 2)}, ("Igor", 66)),
        ({"Alnur": (66, 3), "Ivan": (55, 1)}, ("Alnur", 66)),
    ],
)
def test_search_for_winners(results_dict, winner):
    assert search_for_winners(results_dict) == winner
