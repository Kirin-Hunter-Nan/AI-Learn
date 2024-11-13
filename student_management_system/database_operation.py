import pymysql
import yaml

with open('config.yml', 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

connection = pymysql.connect(**config['mysql'])
cursor = connection.cursor()


class Student:
    def __init__(self):
        self.cursor = cursor

    def get_password(self, stu_id):
        """
        get the password of student and compared it in main.py for students' logging in
        """

        get_password = """
        select stu_password from student where stu_id = %S"""
        self.cursor.execute(get_password, stu_id)
        result: tuple = cursor.fetchone()
        if result is not None:
            stored_password = result[0]
            return stored_password

    def show_information(self, stu_id):
        """
        show the information of student
        """

        show_information = """
        select stu_id, stu_name, stu_phone from student where stu_id = %s"""
        self.cursor.execute(show_information, stu_id)
        result: tuple = cursor.fetchall()
        for r in result:
            return r


class Teacher:
    def __init__(self):
        self.cursor = cursor

    def get_password(self, tea_id):
        """
        get the teacher password and compared it in main.py for teachers' logging in
        """

        get_password = """
        select tea_password from teacher where tea_id = %s """
        self.cursor.execute(get_password, tea_id)
        result: tuple = cursor.fetchone()
        if result is not None:
            stored_password = result[0]
            return stored_password

    def show_information(self, tea_id):
        """
        show the information of teacher
        """

        show_information = """
        select tea_id, tea_name, tea_phone, tea_class from teacher where tea_id = %s"""
        self.cursor.execute(show_information, tea_id)
        result: tuple = cursor.fetchall()
        for r in result:
            return r


class Admin:
    def __init__(self):
        self.cursor = cursor

    def get_password(self, admin_id):
        """
        get the password of admin and compared it in main.py for admin logging in
        """
        get_password = """
        select admin_password from admin where admin_id = %s"""
        self.cursor.execute(get_password, admin_id)
        result: tuple = cursor.fetchone()
        if result is not None:
            stored_password = result[0]
            return stored_password

    def show_information(self, admin_id):
        """
        show the information of the admin
        :return:
        """
        show_information = """
        select admin_id, admin_name, admin_phone from admin where admin_id = %s"""
        self.cursor.execute(show_information, admin_id)
        result: tuple = cursor.fetchall()
        for r in result:
            return r

    def insert_student_information(self, values):
        """
        insert the information of a student
        :return:
        """
        insert_information = """
        insert into student (id, stu_id, stu_name, stu_phone, stu_class, stu_password) values (NULL, %s, %s, %s, %s, %s)"""
        values = values.split(',')
        self.cursor.execute(insert_information, values)

    def insert_teacher_information(self, values):
        """
        insert the information of a teacher
        :return:
        """
        insert_information = """
        insert into teacher (id, tea_id, tea_name, tea_phone, tea_class, tea_password) values (NULL, %s, %s, %s, %s ,%s)"""
        values = values.split(',')
        self.cursor.execute(insert_information, values)

    # def update_student_information(self, stu_id, stu_choice):
    #     """
    #     update the information of a student
    #     :return:
    #     """




# insert_information()
# show_information()
# update_information()
# delete_information()
# print("enter your student id:")
# stu_id = input()
# print(student_password_compared(stu_id))
# admin_id = 'a000001'
# admin_password_compared(admin_id)