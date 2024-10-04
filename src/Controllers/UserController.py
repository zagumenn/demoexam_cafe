from src.Models.Users import *

class UserController():
    # метод авторизации
    def log_in(self, input_login, input_password):

        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False

    def administration(self, input_login, input_password):



if __name__ == "__main__":
    users = UserController()
    print(users.log_in('admin_Ekaterina', '11111'))



