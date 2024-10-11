from tkinter import *

from src.Controllers.OrderController import OrderController
from src.Controllers.UserController import *

def kitchener():

    def update_order_pay(id):
        button_login.configure(text="Оплачен", background='grey')
        order.update_order_pay(id)
        update()

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
    panel_kitchener = Tk() # вызываем класс tkinter
    panel_kitchener.title("Панель повара") # создаём название окна
    panel_kitchener.geometry('1600x800') #  размер окна
    title = Label(panel_kitchener, text="Окно повара", font=("Times New Roman", 24), anchor='center', width=100)
    title.grid(column = 0, row = 0, columnspan = 10, padx = 0, pady = 0) # координаты текста в окне

    # Текст
    title1 = Label(panel_kitchener, text="Столик", font=("Times New Roman", 16), foreground='blue')
    title1.grid(column = 1, row = 1) # координаты текста в окне

    title2 = Label(panel_kitchener, text="Блюда", font=("Times New Roman", 16), foreground='blue')
    title2.grid(column = 2, row = 1) # координаты текста в окне

    title3 = Label(panel_kitchener, text="Количество клиентов", font=("Times New Roman", 16), foreground='blue')
    title3.grid(column = 3, row = 1) # координаты текста в окне

    # кнопки


    # столик, блюда и количество клиентов
    order = OrderController()
    list_order = order.get()
    count_row = 2
    for row in list_order:
        if row.status_id:
            text_tables = Label(panel_kitchener, text=row.table_id.number)
            text_tables.grid(column=1, row=count_row, padx=1, pady=1)
            text_foods = Label(panel_kitchener, text=row.food_id.name)
            text_foods.grid(column=2, row=count_row, padx=0, pady=1)
            text_client = Label(panel_kitchener, text=row.count_cliens)
            text_client.grid(column=3, row=count_row, padx=0, pady=1)
            button_login = Button(panel_kitchener,
                                  text= row.status_id.name,
                                  height=2,
                                  width=8,
                                  background= 'green',
                                  foreground='white',
                                  )
            status_title = Label(panel_kitchener, text=row.id)
            status_title.grid(column=0, row=count_row, padx=0, pady=1)
            button_login.grid(column=4, row=count_row, padx=0, pady=1)

            count_row += 1


    panel_kitchener.mainloop() # запускает окно

if __name__ == "__main__":
    kitchener()