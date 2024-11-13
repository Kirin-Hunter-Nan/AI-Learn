import database_operation

def student_window(student_id):
    print(f"-------------------welcome {student_id} -------------------")
    print(database_operation.show_stu_information(student_id))
