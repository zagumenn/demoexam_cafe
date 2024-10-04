from symbol import shift_expr

from src.Models.Orders import *

class OrderController():

    # Вывод пользователей
    def get(self):
        return  Orders.select().execute()

    def add(self, count_client, table_id, drink_id, food_id, shift_id):
        Orders.create(count_cliens = count_client, table_id = table_id, drink_id = drink_id, food_id = food_id,
                      shift_id = shift_id)

    # Уволить - изменить стату на  False
    def update_order_pay(self, id_order):
        Orders.update({Orders.status_id: 2}).where(Orders.id == id_order).execute()

    def update_order_сooking(self, id_order):
        Orders.update({Orders.status_id: 3}).where(Orders.id == id_order).execute()

    def update_order_ready(self, id_order):
        Orders.update({Orders.status_id: 4}).where(Orders.id == id_order).execute()

    def show(self, shift_id):
        return Orders.select().where(Orders.shift_id == shift_id).execute()

if __name__ == "__main__":
    ord = OrderController()
    #ord.add('5', '1', '1', '1', '2')
    print("-------------")
    for row in ord.get():
        print(row.id, row.count_cliens, row.table_id, row.drink_id, row.food_id, row.shift_id, row.status_id)
    ord.update_order_pay(1)
    ord.update_order_сooking(2)
    ord.update_order_ready(3)
    print("-------------")
    for row in ord.get():
        print(row.id, row.count_cliens, row.table_id, row.drink_id, row.food_id, row.shift_id, row.status_id)
    print("-------------")
for row in ord.show(2):
    print(row.id, row.count_cliens, row.table_id, row.drink_id, row.food_id, row.shift_id, row.status_id)
