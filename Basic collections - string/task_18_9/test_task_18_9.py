import pytest
from task_18_9.task_18_9 import flip_message


@pytest.mark.parametrize(
    ("message", "new_message"),
    [
        ("Это задание", "отЭ еинадаз"),
        (" очень! простое.", " ьнечо! еотсорп."),
        ("Хотя ,. возм:ожно и нет.", "ятоХ ,. мзов:онжо и тен."),
    ],
)
def test_flip_message(message, new_message):
    assert flip_message(message) == new_message
