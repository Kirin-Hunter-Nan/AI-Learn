from database_operation import Admin


admin_instance = Admin()


def admin_window(admin_id):
    print(f"-------------------welcome {admin_id} -------------------")
    print(admin_instance.show_information(admin_id))

    print("Please choose your choice")

### 根据选择，进入不同的系统
# 1学生，2老师，
# 选择1， 对学生进行处理，选择2， 对教师进行处理
