import database_operation


def admin_window(admin_id):
    print(f"-------------------welcome {admin_id} -------------------")
    print(database_operation.show_admin_information(admin_id))
