from database_operation import Student


student_instance = Student()


def student_window(student_id):
    print(f"-------------------welcome {student_id} -------------------")
    print(student_instance.show_information(student_id))

    print("please choose your choice:")
    choice = input()
    if choice == "1":
        print("Course selection")

    if choice == "2":
        print("Exam results")

    if choice == "3":
        print("Drop out")

    if choice == "4":
        print("Log out")