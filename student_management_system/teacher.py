from database_operation import Teacher


teacher_instance = Teacher()


def teacher_window(teacher_id):
    print(f"-------------------welcome {teacher_id} -------------------")
    print(teacher_instance.show_information(teacher_id))
