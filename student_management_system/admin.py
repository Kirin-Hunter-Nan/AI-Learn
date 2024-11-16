from database_operation import Admin


admin_instance = Admin()


def admin_window(admin_id):
    print(f"-------------------welcome {admin_id} -------------------")
    print(admin_instance.show_information(admin_id))
    print("What do you want to do with Student or Teacher")
    print("1. Student")
    print("2. Teacher")

    ### 根据选择，进入不同的系统
    # 1学生，2老师，
    # 选择1， 对学生进行处理，选择2， 对教师进行处理
    print("Please choose your choice")
    choice = input()
    if choice == "1":
        print("Which operation do you want to do:")
        print("1. Show the information of a student")
        print("2. Insert a student")
        print("3. Change the information of a student")
        print("4. Drop a student")
        choice_stu = input()
        if choice_stu == "1":

        if choice_stu == "2":

        if choice_stu == "3":

        if choice_stu == "4":


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

