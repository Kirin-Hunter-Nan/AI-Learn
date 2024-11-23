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
        """
        show_information = """

        select admin_id, admin_name, admin_phone from admin where admin_id = %s"""

        self.cursor.execute(show_information, admin_id)
        result: tuple = cursor.fetchall()
        for r in result:
            return r

    # def student_system(self, choice, id):
    #     """
    #     this is for admin to operate the information of student
    #     :param choice:
    #     :return:
    #     """
    #     if choice == "1":
    #         show_information = """
    #
    #         select stu_id, stu_name, stu_phone, stu_class from student where stu_id = %s"""
    #
    #         self.cursor.execute(show_information, id)
    #
    #     if choice == "2":
    #         insert



    def show_student_information(self, id):
        """
        show the information of a student
        :return:
        """

        show_information = """

        select stu_id, stu_name, stu_phone, stu_class from student where stu_id = %s"""

        self.cursor.execute(show_information, id)

    def show_teacher_information(self, id):
        """
        show the information of a teacher
        :param id:
        :return:
        """

        show_information = """

        select tea_id, tea_name, tea_phone, tea_class from teacher where tea_id = %s"""

        self.cursor.execute(show_information, id)

    def insert_student_information(self, values):
        """
        insert the information of a student
        """
        insert_information = """

        insert into student (id, stu_id, stu_name, stu_phone, stu_class, stu_password) values (NULL, %s, %s, %s, %s, %s)"""

        values = values.split(',')
        self.cursor.execute(insert_information, values)

    def insert_teacher_information(self, values):
        """
        insert the information of a teacher
        """
        insert_information = """

        insert into teacher (id, tea_id, tea_name, tea_phone, tea_class, tea_password) values (NULL, %s, %s, %s, %s ,%s)"""

        values = values.split(',')
        self.cursor.execute(insert_information, values)

    def update_student_information(self, choice, stu_id, new_information, ):
        """
        update the information of a student
        :param choice:
        :param stu_id:
        :param new_information
        """

        # update the student name in the database
        if choice == "1 ":
            update_information = """

            update student set stu_name = %s where stu_id = %s"""

            values = (new_information, stu_id)
            self.cursor.execute(update_information, values)

        # update the student phone number in the database
        if choice == "2":
            update_information = """

            update student set stu_phone = %s where stu_id = %s"""

            values = (new_information, stu_id)
            self.cursor.execute(update_information, values)

        # update the student class in the database
        if choice == "3":
            update_information = """

            update student set stu_class = %s where stu_id = %s"""

            values = (new_information, stu_id)
            self.cursor.execute(update_information, values)

        # update the student password in the database
        if choice == "4":
            update_information = """

            update student set stu_password = %s where stu_id = %s"""

            values = (new_information, stu_id)
            self.cursor.execute(update_information, values)

    def update_teacher_information(self, choice, new_information, tea_id):
        """
        update the information of a teacher
        :param choice:
        :param new_information:
        :param tea_id:
        :return:
        """

        if choice == "1":
            update_information = """

            update teacher set tea_name = %s where tea_id = %s"""

            values = (new_information, tea_id)
            self.cursor.execute(update_information, values)

        if choice == "2":
            update_information = """

            update teacher set tea_phone = %s where tea_id = %s"""

            values = (new_information, tea_id)
            self.cursor.execute(update_information, values)

        if choice == "3":
            update_information = """

            update teacher set tea_class = %s where tea_id = %s"""

            values = (new_information, tea_id)
            self.cursor.execute(update_information, values)

        if choice == "4":
            update_information = """

            update teacher set tea_password = %s where tea_id = %s"""

            values = (new_information, tea_id)
            self.cursor.execute(update_information, values)

    def update_admin_information(self, choice, new_information, admin_id):
        """
        update the information of a admin
        """

        if choice == "1":
            update_information = """

            update admin set admin_name = %s where admin_id = %s"""

            values = (new_information, admin_id)
            self.cursor.execute(update_information, values)

        if choice == "2":
            update_information = """

            update admin set admin_phone = %s where admin_id = %s"""

            values = (new_information, admin_id)
            self.cursor.execute(update_information, values)

        if choice == "3":
            update_information = """

            update admin set admin_password = %s where admin_id = %s"""

            values = (new_information, admin_id)
            self.cursor.execute(update_information, values)

    def delete_information(self, choice, id):
        """
        if choice == 1
        it will delete the information of a student

        elif choice == 2
        it will delete the information of a teacher
        :param choice:
        :param id:
        :return:
        """
        if choice == "1":
            delete_information = """

            delete from student where stu_id = %s"""

            self.cursor.execute(delete_information, id)

        if choice == "2":
            delete_information = """

            delete from teacher where tea_id = %s"""

            self.cursor.execute(delete_information, id)


# insert_information()
# show_information()
# update_information()
# delete_information()
# print("enter your student id:")
# stu_id = input()
# print(student_password_compared(stu_id))
# admin_id = 'a000001'
# admin_password_compared(admin_id)