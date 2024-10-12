# Окно - Панель Администратора
from tkinter import *
from tkinter import ttk
from src.Controllers.UserController import UserController
from src.Controllers.ShiftController import ShiftController

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

    def add_shift(date, cook, officiant_1, officiant_2):
        shift.add(date, cook, officiant_1, officiant_2)
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
    shift = ShiftController()
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

        # Добавить смену

        input_shift = Entry(panel_admin, width=40)
        name_input_shift = Label(panel_admin, text="Введите смену ")
        name_input_shift.grid(column=6, row=2)
        input_shift.grid(column=6, row=3)

        input_cook = Entry(panel_admin, width=40)
        name_input_cook = Label(panel_admin, text="Введите повара ")
        list_cook = UserController.list_user(2)
        combobox_cook = ttk.Combobox(values=list_cook, width=40)
        combobox_cook.grid(column = 7, row = 5)
        name_input_cook.grid(column=6, row=4)
        input_cook.grid(column=6, row=5)

        input_waiter1 = Entry(panel_admin, width=40)
        list_waiter1 = UserController.list_user(3)
        combobox_waiter1 = ttk.Combobox(values=list_waiter1, width=40)
        combobox_waiter1.grid(column=7, row=7)
        name_input_waiter1 = Label(panel_admin, text="Введите первого официанта")
        name_input_waiter1.grid(column=6, row=6)
        input_waiter1.grid(column=6, row=7)

        input_waiter2 = Entry(panel_admin, width=40)
        list_waiter2 = UserController.list_user(3)
        combobox_waiter2 = ttk.Combobox(values=list_waiter2, width=40)
        combobox_waiter2.grid(column=7, row=9)
        name_input_waiter2 = Label(panel_admin, text="Введите второго официанта")
        name_input_waiter2.grid(column=6, row=8)
        input_waiter2.grid(column=6, row=9)


        button_add_user = Button(panel_admin, text="Добавить пользователя", height=2, width=20,
                                 background='blue', foreground='white', command = lambda: add_user(input_login.get(), input_password.get(),
                                                                                                    input_name.get(), input_role.get()))

        button_add_shift = Button(panel_admin, text="Добавить смену", height=2, width=20,
                                 background='blue', foreground='white',
                                 command=lambda: add_shift(input_shift.get(), input_cook.get(),
                                                          input_waiter1.get(), input_waiter2.get()))

        button_add_shift_1 = Button(panel_admin, text="Добавить смену", height=2, width=20,
                                  background='blue', foreground='white',
                                  command=lambda: add_shift(input_shift.get(), combobox_cook.get(),
                                                            combobox_waiter1.get(), combobox_waiter2.get()))

        button_add_user.grid(column = 5, row = 10)
        button_add_shift.grid(column=6, row=10)
        button_add_shift_1.grid(column=7, row=10)




    panel_admin.mainloop()
if __name__ == "__main__":
    admin()
