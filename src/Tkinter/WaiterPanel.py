from tkinter import *

from src.Controllers.OrderController import OrderController
from src.Controllers.UserController import *

def kitchener():

    def update_order_pay(id):
        button_login.configure(text="Оплачен", background='grey')
        order.update_order_pay(id)
        update()

    def add_order(table, food, count_clients):
        order.add_order(table, food, count_clients)
        panel_waiter.after(1000, update)

    def update_update_сooking(id):
        button_login.configure(text="Готовится", background='grey')
        order.update_order_сooking(id)
        update()

    def update_update_ready(id):
        button_login.configure(text="Готов", background='grey')
        order.update_order_ready(id)
        update()


    def update():
        kitchener().destroy()
        kitchener()



# Оформление окна
    panel_waiter = Tk() # вызываем класс tkinter
    panel_waiter.title("Панель официанта") # создаём название окна
    panel_waiter.geometry('1600x800') #  размер окна
    title = Label(panel_waiter, text="Окно официанта", font=("Times New Roman", 24), anchor='center', width=100)
    title.grid(column = 0, row = 0, columnspan = 10, padx = 0, pady = 0) # координаты текста в окне

    # Текст
    title1 = Label(panel_waiter, text="Столик", font=("Times New Roman", 16), foreground='blue')
    title1.grid(column = 1, row = 1) # координаты текста в окне

    title2 = Label(panel_waiter, text="Блюда", font=("Times New Roman", 16), foreground='blue')
    title2.grid(column = 2, row = 1) # координаты текста в окне

    title3 = Label(panel_waiter, text="Количество клиентов", font=("Times New Roman", 16), foreground='blue')
    title3.grid(column = 3, row = 1) # координаты текста в окне

    # кнопки


    # столик, блюда и количество клиентов
    order = OrderController()
    list_order = order.get()
    count_row = 2
    for row in list_order:
        if row.status_id:
            text_tables = Label(panel_waiter, text=row.table_id.number)
            text_tables.grid(column=1, row=count_row, padx=1, pady=1)
            text_foods = Label(panel_waiter, text=row.food_id.name)
            text_foods.grid(column=2, row=count_row, padx=0, pady=1)
            text_client = Label(panel_waiter, text=row.count_cliens)
            text_client.grid(column=3, row=count_row, padx=0, pady=1)
            button_login = Button(panel_waiter,
                                  text= row.status_id.name,
                                  height=2,
                                  width=8,
                                  background= 'green',
                                  foreground='white',
                                  )
            status_title = Label(panel_waiter, text=row.id)
            status_title.grid(column=0, row=count_row, padx=0, pady=1)
            button_login.grid(column=4, row=count_row, padx=0, pady=1)

            count_row += 1

    input_table = Entry(panel_waiter, width=40)
    name_input_table = Label(panel_waiter, text="Введите столик ")
    name_input_table.grid(column=5, row=1)
    input_table.grid(column=5, row=2)

    input_food = Entry(panel_waiter, width=40)
    name_input_food = Label(panel_waiter, text="Введите блюда ")
    name_input_food.grid(column=5, row=3)
    input_food.grid(column=5, row=4)

    input_clients = Entry(panel_waiter, width=40)
    name_input_clients = Label(panel_waiter, text="Введите количество клиентов")
    name_input_clients.grid(column=5, row=5)
    input_clients.grid(column=5, row=6)

    button_add_user = Button(panel_waiter, text="Добавить заказ", height=2, width=20,
                             background='blue', foreground='white',
                             command=lambda: add_order(input_table.get(), input_food.get(),
                                                      input_clients.get()))

    button_add_user.grid(column=5, row = 7)


    panel_waiter.mainloop() # запускает окно

if __name__ == "__main__":
    kitchener()