from task_18_10.task_18_10 import decipher_with_caesar_cipher, shift_character_position


def test_decipher_with_caesar_cipher():
    assert decipher_with_caesar_cipher("vujgvmCfb tj ufscfu ouib z/vhm ", -1) == [
        "utifulBea",
        "si",
        "terbet",
        "ntha",
        "y.ugl",
    ]


def test_shift_character_position():
    assert shift_character_position(
        ["icitExpl", "is", "erbett", "than", "icit.impl"], -4
    ) == ["Explicit", "is", "better", "than", "implicit."]
