from peewee import *

connect = MySQLDatabase(
"ZagS1234_dem_cafe",
    user = 'ZagS1234_adcafe',
    password = '111111',
    host = '10.11.13.118',
    port = 3306
)


if __name__ == '__main__':
    connect.connect()