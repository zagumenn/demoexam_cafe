# Модель описывающая сущьность из таблицы столы
from src.Models.Base import *

class Foods(Base):
    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()