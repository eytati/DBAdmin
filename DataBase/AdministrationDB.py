from DataBase import Connection

class AdministrationDB:

    connection: None

    def __init__(self):
        get_connection= Connection.DBConnection()
        self.connection = get_connection.returnInstance()

    def CreateDB(self, name,
                 owner = 'postgres',
                 template = 'template0',
                 encoding = 'UTF8',
                 collate = 'C',
                 type = 'C',
                 table_space = 'pg_default',
                 connection= -1):
        try:
            data = "CREATE DATABASE " +name+" WITH OWNER = "+owner+" TEMPLATE = "+ template+" ENCODING = "+encoding+" LC_COLLATE = "+ collate+ " LC_CTYPE = "+type+" TABLESPACE = "+table_space+" CONNECTION LIMIT = "+connection
            self.connection.autocommit = True
            cursor = self.connection.cursor(data)
            cursor.execute()
            print("Base de datos creada con exito")
        except:
            print('')

    def GetDB(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT table_name
                                  FROM information_schema.tables
                                  WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema'); """)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

    def DeleteDB(self, db_name):
        try:
            data= "Drop DATABASE "+db_name
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(data)
        except:
            print("No se elimino base de datos")

class UpdateDataBase:

    def __init__(self):
        get_connection= Connection.DBConnection()
        self.connection = get_connection.returnInstance()

    def RenameDB(self, name_db, new_name):
        try:
            data = "ALTER DATABASE "+name_db+" RENAME TO "+new_name
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print("Renombramiento de dase de datos exitoso")
        except:
            print("No se renombro dase de datos")

    def ChangeOwner(self, name_db, new_owner):
        try:
            data= "ALTER DATABASE "+name_db+" OWNER TO "+new_owner
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print("cambio de usuario exitoso")
        except:
            print("No se edito usuario")

    def ChangeConnections(self, name_db, connections):
        try:
            data= "ALTER DATABASE "+name_db+" WITH CONNECTION LIMIT = "+connections
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print("Actualizacion numero de conxiones fue exitoso")
        except:
            print("No se actualizo el numero de conexiones")
