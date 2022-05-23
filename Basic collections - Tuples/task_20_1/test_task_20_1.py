from task_20_1.task_20_1 import (
    create_list_of_id_and_age,
    create_set_of_interests_and_total_lenght_of_surnames,
)

students = {
    1: {
        "name": "Bob",
        "surname": "Vazovski",
        "age": 23,
        "interests": ["biology", "swimming"],
    },
    2: {
        "name": "Rob",
        "surname": "Stepanov",
        "age": 24,
        "interests": ["math", "computer games", "running"],
    },
    3: {
        "name": "Alexander",
        "surname": "Krug",
        "age": 22,
        "interests": ["languages", "health food"],
    },
}


def test_create_list_of_id_and_age():
    assert create_list_of_id_and_age(students) == [(1, 23), (2, 24), (3, 22)]


def test_create_set_of_interests_and_total_lenght_of_surnames():
    assert create_set_of_interests_and_total_lenght_of_surnames(students) == (
        {
            "running",
            "computer games",
            "math",
            "languages",
            "biology",
            "swimming",
            "health food",
        },
        20,
    )
