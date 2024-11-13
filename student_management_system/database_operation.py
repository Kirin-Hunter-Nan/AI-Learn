import pymysql
import yaml

with open('config.yml', 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

connection = pymysql.connect(**config['mysql'])

cursor = connection.cursor()


def insert_information():
    """
    insert information into the student table.
    """
    insert_student_information = """
        insert into student(id, stu_id, stu_name, stu_phone, stu_class) values(NULL, %s, %s, %s, %s)"""

    user_input = input("Enter your information:")
    values = user_input.split(',')
    print(values)
    cursor.execute(insert_student_information, values)


def update_information():
    """
    update the information into the student table.
    """
    update_student_class_information = """
    update student set stu_class = %s where stu_id = %s"""

    print("请输入您的学号：")
    student_id = input()
    print("请输入您要修改的课程：")
    student_class = input()
    values = (student_class, student_id)
    cursor.execute(update_student_class_information, values)


def delete_information():
    delete_student_information = """
    delete from student where stu_id = %s"""
    print("请输入您要开除的学生学号：")
    stu_id = input()
    cursor.execute(delete_student_information, stu_id)


def student_password_compared(stu_id):
    compared = """
    select stu_password from student where stu_id = %s"""
    cursor.execute(compared, stu_id)
    result: tuple = cursor.fetchone()

    if result is not None:
        stored_password = result[0]
        return stored_password


def teacher_password_compared(tea_id):
    compared = """
    select tea_password from teacher where tea_id = %s"""
    cursor.execute(compared, tea_id)
    result: tuple = cursor.fetchone()

    if result is not None:
        stored_password = result[0]
        return stored_password


def admin_password_compared(admin_id):
    compared = """
    select admin_password from admin where admin_id = %s"""
    cursor.execute(compared, admin_id)
    result: tuple = cursor.fetchone()

    if result is not None:
        stored_password = result[0]
        return stored_password



def show_stu_information(student_id):
    show_student_information = """
    select stu_id, stu_name, stu_phone, stu_class from student where stu_id = %s"""
    values = student_id
    cursor.execute(show_student_information, values)
    result: tuple = cursor.fetchall()
    for r in result:
        return r


def show_tea_information(teacher_id):
    show_teacher_information = """
    select tea_id, tea_name, tea_phone, tea_class from teacher where tea_id = %s"""
    values = teacher_id
    cursor.execute(show_teacher_information, values)
    result: tuple = cursor.fetchall()
    for r in result:
        return r


def show_admin_information(admin_id):
    show_admin_information = """
    select admin_id, admin_name, admin_phone from admin where admin_id = %s"""
    cursor.execute(show_admin_information, admin_id)
    result: tuple = cursor.fetchall()
    for r in result:
        return r



# insert_information()
# show_information()
# update_information()
# delete_information()
# print("enter your student id:")
# stu_id = input()
# print(student_password_compared(stu_id))
# admin_id = 'a000001'
# admin_password_compared(admin_id)