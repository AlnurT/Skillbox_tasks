import pytest
from Task_20_8.task_20_8 import add_contact, search_contact

t_book = {
    ("Alnur", "Tazhbenov"): 999,
    ("Talgat", "Shugabaev"): 777,
    ("Kairat", "Tazhbenov"): 666,
}


@pytest.mark.parametrize(
    ("telephone_book", "telephone_book_with_person"),
    [
        (t_book, t_book),
        ({}, {("Alnur", "Tazhbenov"): 999}),
    ],
)
def test_add_contact(telephone_book, telephone_book_with_person):
    assert (
        add_contact(telephone_book, ("Alnur", "Tazhbenov"), 999)
        == telephone_book_with_person
    )


@pytest.mark.parametrize(
    ("telephone_book", "surname", "found_contacts"),
    [
        (
            t_book,
            "Tazhbenov",
            {("Alnur", "Tazhbenov"): 999, ("Kairat", "Tazhbenov"): 666},
        ),
        (t_book, "Shugabaev", {("Talgat", "Shugabaev"): 777}),
        (t_book, "Solomonov", {}),
    ],
)
def test_search_contact(telephone_book, surname, found_contacts):
    assert search_contact(telephone_book, surname) == found_contacts
