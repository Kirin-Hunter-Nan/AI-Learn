from database_operation import Admin


admin_instance = Admin()


def admin_window(admin_id):
    print(f"-------------------welcome {admin_id} -------------------")
    print(admin_instance.show_information(admin_id))
