# Окно - Панель Администратора
from tkinter import *
from src.Controllers.UserController import UserController


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
                          command = user.update_status(row.id))
    button_login.grid(column = 3, row = count_row, padx = 0, pady = 1)

    print(row.login, row.status)
    count_row += 1


panel_admin.mainloop()
