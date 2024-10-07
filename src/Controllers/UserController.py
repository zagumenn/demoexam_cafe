from src.Models.Users import *

class UserController():
    # метод авторизации
    def log_in(self, input_login, input_password):

        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False

    # Вывод пользователей
    def get(self):
        return  Users.select().execute()

    def add(self, input_login, input_password, input_name, input_role_id):
        Users.create(login = input_login, password = input_password, name = input_name, role_id = input_role_id)

    # Уволить - изменить стату на  False
    def update_status(self, id_user):
        Users.update({Users.status: False}).where(Users.id == id_user).execute()

    # Метод класса
    @classmethod
    # Метод который выводит id по имени
    def show(cls, login):
        return Users.get(Users.login == login)

if __name__ == "__main__":
    users = UserController()
    print(users.log_in('admin_Ekaterina', '11111'))
    for row in users.get():
        print(row.id, row.login, row.password, row.name, row.status)
    users.add('Van', '1234', 'Vana', '2')
    print("-----------------")
    for row in users.get():
        print(row.id, row.name, row.status)
    users.update_status(9)
    print("-----------------")
    for row in users.get():
        print(row.id, row.name, row.status)
    print(users.show('Van'))