from tkinter import *
from src.Controllers.UserController import *



# Оформление окна
window = Tk() # вызываем класс tkinter
window.title("Информационная система Кафе") # создаём название окна
window.geometry('800x600') #  размер окна
title = Label(window, text="Окно повара", font=("Times New Roman", 24))
title.grid(column = 4, row = 0) # координаты текста в окне

# Текст
title1 = Label(window, text="Столик", font=("Times New Roman", 16), foreground='blue')
title1.grid(column = 0, row = 1) # координаты текста в окне

title2 = Label(window, text="Блюда", font=("Times New Roman", 16), foreground='blue')
title2.grid(column = 4, row = 1) # координаты текста в окне

title3 = Label(window, text="Количество клиентов", font=("Times New Roman", 16), foreground='blue')
title3.grid(column = 5, row = 1) # координаты текста в окне

# кнопки
button_cook1 = Button(window, text="Готовится", height = 1, width = 10, background = 'green', foreground = 'white')
button_cook1.grid(column = 6, row = 2)
button_cook2 = Button(window, text="Готовится", height = 1, width = 10, background = 'green', foreground = 'white')
button_cook2.grid(column = 6, row = 3)
button_cook3 = Button(window, text="Готовится", height = 1, width = 10, background = 'green', foreground = 'white')
button_cook3.grid(column = 6, row = 4)
button_cook4 = Button(window, text="Готовится", height = 1, width = 10, background = 'green', foreground = 'white')
button_cook4.grid(column = 6, row = 5)

window.mainloop() # запускает окно