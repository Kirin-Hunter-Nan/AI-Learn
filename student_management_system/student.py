import database_operation


def student_window(student_id):
    print(f"-------------------welcome {student_id} -------------------")
    print(database_operation.show_stu_information(student_id))

    print("please choose your choice:")
    choice = input()
    if choice == "1":
        print("进入学生选课系统")

    if choice == "2":
        print("进入成绩查询系统")

    if choice == "3":
        print("退学")
