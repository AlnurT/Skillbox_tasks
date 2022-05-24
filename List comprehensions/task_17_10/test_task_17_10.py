import pytest
from task_17_10.task_17_10 import create_alphabet, encrypt_text

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def test_create_alphabet():
    assert create_alphabet() == alphabet


@pytest.mark.parametrize(
    ("shift", "cypher"), [(0, "это питон!"), (3, "ахс тлхср!"), (-9, "фйе жяйед!")]
)
def test_encrypt_text(shift, cypher):
    assert encrypt_text("это питон!", shift, alphabet) == cypher
