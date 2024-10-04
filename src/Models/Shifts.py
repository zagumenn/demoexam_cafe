# Модель описывающая сущьность из таблицы столы
from src.Models.Base import *
from src.Models.Users import Users


class Shifts(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    cook_id = ForeignKeyField(Users)
    oficiant_1_id = ForeignKeyField(Users)
    oficiant_2_id = ForeignKeyField(Users)