# Окно - Панель Администратора
from tkinter import *
from src.Controllers.UserController import UserController


# функционал
# создание диалогового окна
def admin():

    def status_false(id):
        button_login.configure(text="Уволен", background='grey')
        user.update_status(id)
        update()

    def add_user(login, password, name, role):
        user.add(login, password, name, role)
        panel_admin.after(1000, update)

    def update():
        panel_admin.destroy()
        admin()


    panel_admin = Tk()
    panel_admin.geometry('1600x800')
    panel_admin.title("Панель администратора")

    title_window = Label(panel_admin, text='Панель администратора', font=("Times New Roman", 24), anchor='center', width= 100)
    title_window.grid(column = 0, row = 0, columnspan = 10, padx = 0, pady = 0)
    #title_window.grid(column = 0, row = 0, padx = 400, pady = 10)
    #title_window.grid(expand = True, anchor = N)

    # Сотрудники
    title_employee = Label(panel_admin, text='Сотрудники', font=("Times New Roman", 20))
    #title_employee.pack(expand = True, anchor = NW, side = TOP)
    title_employee.grid(column = 1, row = 1, padx = 10, pady = 10)

    title_role = Label(panel_admin, text='Должность', font=("Times New Roman", 20))
    #title_employee.pack(expand = True, anchor = NW, side = TOP)
    title_role.grid(column = 2, row = 1, padx = 10, pady = 10)

    # логин должность и кнопка
    user = UserController()
    list_user = user.get()
    count_row = 2
    for row in list_user:
        if row.status:
            login_title = Label(panel_admin, text = row.name)
            login_title.grid(column = 1, row = count_row, padx = 1, pady = 1)
            login_role = Label(panel_admin, text=row.role_id.role)
            login_role.grid(column=2, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                                  text = "Уволить",
                                  height = 2,
                                  width = 8,
                                  background = 'red',
                                  foreground = 'white',
                                  command = lambda id = row.id: status_false(id))
            status_title = Label(panel_admin, text=row.id)
            status_title.grid(column = 0 , row = count_row, padx = 0, pady = 1)
            button_login.grid(column = 3, row = count_row, padx = 0, pady = 1)
        #count_row += 1
        else:
            login_title = Label(panel_admin, text=row.name)
            login_title.grid(column=1, row=count_row, padx=1, pady=1)
            login_role = Label(panel_admin, text=row.role_id.role)
            login_role.grid(column=2, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                              text="Уволен",
                              height=2,
                              width=8,
                              background='grey',
                              foreground='white',
                              command=lambda id=row.id: status_false(id))
        status_title = Label(panel_admin, text=row.id)
        status_title.grid(column=0, row=count_row, padx=0, pady=1)
        button_login.grid(column=3, row=count_row, padx=0, pady=1)

        count_row += 1
        print(row.login, row.status)

        # Добавить пользователя

        input_login = Entry(panel_admin, width=40)
        name_input_login = Label(panel_admin, text="Введите логин ")
        name_input_login.grid(column=5, row=2)
        input_login.grid(column=5, row=3)

        input_name = Entry(panel_admin, width=40)
        name_input_name = Label(panel_admin, text = "Введите имя ")
        name_input_name.grid(column = 5, row = 4)
        input_name.grid(column = 5, row = 5)

        input_password = Entry(panel_admin, width=40)
        name_input_password = Label(panel_admin, text="Введите пароль")
        name_input_password.grid(column = 5, row=6)
        input_password.grid(column = 5, row = 7)

        input_role = Entry(panel_admin, width=40)
        name_input_role = Label(panel_admin, text="Введите должность")
        name_input_role.grid(column = 5, row = 8)
        input_role.grid(column = 5, row = 9)

        button_add_user = Button(panel_admin, text="Добавить пользователя", height=2, width=20,
                                 background='blue', foreground='white', command = lambda: add_user(input_login.get(), input_password.get(),
                                                                                                    input_name.get(), input_role.get()))

        button_add_user.grid(column = 5, row = 10)



    panel_admin.mainloop()
if __name__ == "__main__":
    admin()
