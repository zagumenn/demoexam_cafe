# Модель описывающая сущьность из таблицы столы
from src.Models.Base import *

class Roles(Base):
    id = PrimaryKeyField()
    role = CharField()
