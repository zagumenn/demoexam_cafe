# Окно авторизации с помощью библиотеки TKinter

from tkinter import *
from src.Controllers.UserController import *

# Функционал
def click_test():
    button_login.configure(text="Клик")
    message.configure(text=log_in.get(), font = (16), foreground='red')
    log_in.select_clear()

# функция авторизации
def login():
    user = UserController()
    result = user.log_in(log_in.get(), passwd_in.get())
    print(result)
    if result:
        log = UserController.show(log_in.get()).role_id.id
        if log == 1:
            print("Админ")
        elif log == 2:
            print("Повар")
        else:
            print("Официант")
    else:
        print("Пароль или логин введены не верно")

# Оформление окна
window = Tk() # вызываем класс tkinter
window.title("Информационная система Кафе") # создаём название окна
window.geometry('800x600') #  размер окна
title = Label(window, text="Приветствуем в информационнной системе Кафе", font=("Times New Roman", 24))
title.grid(column = 0, row = 0) # координаты текста в окне

# кнопки
button_login = Button(window, text="Войти", height = 1, width = 10, background = 'blue', foreground = 'white', command = login)
button_login.grid(column = 0, row = 1)
message = Label(text = '!!!')
message.grid(column = 0, row=4)

# окна ввода данных
log_title = Label(window, text = "Введите логин")
log_title.grid(column = 0, row = 5)
log_in = Entry(window, width = 20)
log_in.grid(column = 1, row = 5)
passwd_title = Label(window, text="Введите пароль")
passwd_title.grid(column = 0, row = 6)
passwd_in = Entry(window, width=20)
passwd_in.grid(column = 1, row =6)



window.mainloop() # запускает окно