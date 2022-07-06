from task_18_6.task_18_6 import encode_string


def test_encode_string():
    assert encode_string("aAAbbсaaaA") == "a1A2b2с1a3A1"
