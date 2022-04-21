def function(my_dict):
    lst = []
    cnt = 0
    for id_student, dict_student in my_dict.items():
        lst += (dict_student['interests'])
        cnt += len(dict_student['surname'])

    return lst, cnt


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
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

pairs_list = [(i_student, i_dict['age']) for i_student, i_dict in students.items()]
print("Список пар: {my_list}".format(my_list=pairs_list))

my_lst, length = function(students)
print("\nСписок интересов всех студентов: {student_list}".format(student_list=my_lst))
print("Общая длина всех фамилий студентов: {length_list}".format(length_list=length))

# зачёт!
