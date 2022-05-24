import pytest
from task_19_6.task_19_6 import search_synonyms

synonyms_dict = {
    1: ["привет", "здравствуйте"],
    2: ["печально", "грустно"],
    3: ["весело", "радостно"],
}


@pytest.mark.parametrize(
    ("word", "result"),
    [
        ("интересно", "Такого слова в словаре нет."),
        ("привет", "Синоним: здравствуйте"),
        ("радостно", "Синоним: весело"),
    ],
)
def test_search_synonyms(word, result):
    assert search_synonyms(synonyms_dict, word) == result
