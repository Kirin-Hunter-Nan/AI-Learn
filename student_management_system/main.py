import student
import teacher
import admin
from database_operation import Student, Teacher, Admin

student_instance = Student()
teacher_instance = Teacher()
admin_instance = Admin()


print("-------------------Student Management System-------------------")
print("1. Student log in")
print("2. Teacher log in")
print("3. Admin log in")
user_input = input("Enter your choice: ")


if user_input == "1":
    """
    This is for student log in, and if successful log in, it will show the window about
    the information of the student and the tools that student can use
    """
    print("-------------------Welcome to Student Management System-------------------")
    print("Please enter your student ID")
    student_id = input("Enter your student ID: ")
    student_password = input("Enter your student password: ")

    if student_password == student_instance.get_password(student_password):
        student.student_window(student_id)

    else:
        print("wrong password,please try again")


if user_input == "2":
    """
    This is for teacher log in, and if successful log in, it will show the window about
    the information of the teacher and the tools that teacher can use
    """
    print("------------------Welcome to Teacher Management System-------------------")
    print("Please enter your teacher ID")
    teacher_id = input("Enter your teacher ID: ")
    teacher_password = input("Enter your teacher password: ")

    if teacher_password == teacher_instance.get_password(teacher_id):
        teacher.teacher_window(teacher_id)

    else:
        print("wrong password,please try again")


if user_input == "3":
    """
    This is for admin log in, and if successful log in, it will show the window about
    the information of the admin and the tools that admin can use
    """
    print("------------------Welcome to Admin Management System-------------------")
    print("Please enter your admin ID")
    admin_id = input("Enter your admin ID: ")
    admin_password = input("Enter your admin password: ")

    if admin_password == admin_instance.get_password(admin_id):
        admin.admin_window(admin_id)

    else:
        print("wrong password,please try again")