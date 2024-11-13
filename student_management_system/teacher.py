import database_operation


def teacher_window(teacher_id):
    print(f"-------------------welcome {teacher_id} -------------------")
    print(database_operation.show_tea_information(teacher_id))
