import psycopg2

class DBConnection:
    instance = None
    connection = None

    def __init__(self):
        if not self.instance:
            self.con = psycopg2.connect("host='localhost' dbname='Prueba' user='postgres' password='hola'")

    def returnInstance(self):
        return self.con