from database_operation import Admin


admin_instance = Admin()


def admin_window(admin_id):
    print(f"-------------------welcome {admin_id} -------------------")
    print(admin_instance.show_information(admin_id))
    print("What do you want to do with Student or Teacher")
    print("1. Student")
    print("2. Teacher")

    ### 根据选择，进入不同的系统
    # 1学生，2老师，3管理员
    # 选择1， 对学生进行处理，选择2， 对教师进行处理
    print("Please choose your choice")
    choice = input("Enter your choice:")
    if choice == "1":
        print("Which operation do you want to do:")
        print("1. Show the information of a student")
        print("2. Insert a student")
        print("3. Change the information of a student")
        print("4. Drop a student")
        choice_stu = input()
        #show the information of student
        if choice_stu == "1":
            stu_id = input("Enter the student id:")
            print(admin_instance.show_student_information(stu_id))
        #insert a student information
        if choice_stu == "2":
            stu_value = input("Enter the student information")
            if admin_instance.insert_student_information(stu_value):
                print("Insert successfully!")
            else:
                print("Insert unsuccessfully, please insert again!")
        if choice_stu == "3":
            operate = input("Please choose the information you want to change:")
            #update the name of a student
            if operate == "1":
                stu_id = input("Enter the student ID:")
                stu_value = input("Enter the new name of a student:")
                admin_instance.update_student_information(operate, stu_id, stu_value)

            #update the phone number of a student
            if operate == "2":
                stu_id = input("Enter the student ID:")
                stu_value = input("Enter the new phone number of a student:")
                admin_instance.update_student_information(operate, stu_id, stu_value)

            #update the class of a student
            if operate == "3":
                stu_id = input("Enter the student ID:")
                stu_value = input("Enter the new class of a student:")
                admin_instance.update_student_information(operate, stu_id, stu_value)

            #update the new password of a student
            if operate == "4":
                stu_id = input("Enter the student ID:")
                stu_value = input("Enter the new password of a student:")
                admin_instance.update_student_information(operate, stu_id, stu_value)

    if choice == "2":
        print("Which operation do you want to do:")
        print("1. Show the information of a teacher")
        print("2. Insert a teacher")
        print("3. Change the information of a teacher")
        print("4. Drop a teacher")

        choice_tea = input()
        if choice_tea == "1":

        if choice_tea == "2":

        if choice_tea == "3":

        if choice_tea == "4":

