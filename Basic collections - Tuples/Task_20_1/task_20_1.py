"""Задача 1. Ревью кода

Ваня работает middle-разработчиком на Python в IT-компании.
Один кандидат на позицию junior-разработчика прислал ему код тестового задания.

В задании был словарь из трёх студентов. Необходимо:
1) Вывести на экран список пар «ID студента — возраст».
2) Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения:
полный список интересов всех студентов и общую длину всех фамилий студентов.

Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.
Ваня — очень придирчивый программист, и после просмотра кода он понял,
что этого кандидата на работу не возьмёт, хотя он выдаёт верный результат. Вот код кандидата:

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt

pairs = []
for i in students:
    pairs += (i, students[i]['age'])

my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (только если очень захочется).
Убедитесь, что программа верно работает Проверки на существование записей в словаре не обязательны, но приветствуются.

Результат работы программы:
Список пар "ID студента — возраст": [(1, 23), (2, 24), (3, 22)]
Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
Общая длина всех фамилий студентов: 20
"""

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


def create_list_of_id_and_age(students: dict) -> list:
    id_and_age_list = []
    for ide, info in students.items():
        id_and_age_list.append((ide, info["age"]))
    return id_and_age_list


def create_set_of_interests_and_total_lenght_of_surnames(students: dict) -> tuple:
    total_lenght = 0
    interests_list = []
    for info in students.values():
        interests_list.extend(info["interests"])
        total_lenght += len(info["surname"])
    return set(interests_list), total_lenght


def main():
    print(f'Список пар "ID студента — возраст": {create_list_of_id_and_age(students)}')
    print(
        f"Полный список интересов всех студентов: {create_set_of_interests_and_total_lenght_of_surnames(students)[0]}"
    )
    print(
        f"Общая длина всех фамилий студентов: {create_set_of_interests_and_total_lenght_of_surnames(students)[1]}"
    )


if __name__ == "__main__":
    main()
