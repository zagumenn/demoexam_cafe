# Модель описывающая сущьность из таблицы столы
from src.Models.Base import *

class Drinks(Base):
    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()
