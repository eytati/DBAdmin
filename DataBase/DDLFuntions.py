from DataBase import Connection

class AdministrationTables:

    def __init__(self):
        get_connection= Connection.DBConnection()
        self.connection = get_connection.returnInstance()

    def CreateTables(self, table_name, create_table):
        data = "Create table "+ table_name+" ("+ create_table+")"
        cursor = self.connection.cursor()
        cursor.execute(data)
        self.connection.commit()

    def GetTables(self, table_name):
        try:
            data = "\"\"select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = '" +table_name+"\"\""
            cursor = self.connection.cursor(data)
            cursor.execute()
            rows = cursor.fetchall()
            for row in rows:
                print(row[0])
        except:
            print("Error al obtener tabla")

    def DeleteTables(self, table_name):
        try:
            data = "Drop table "+table_name
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print("Tabla eliminada con exito")
        except:
            print("No se pudo eliminar tabla")

class UpdateTables:

    def __init__(self):
        get_connection = Connection.DBConnection()
        self.connection = get_connection.returnInstance()

    def AddColumn(self, name_table, name_column, type):
        try:
            cursor = self.connection.cursor()
            data = "alter table "+name_table+" add column "+name_column+" "+ type
            cursor.execute(data)
            self.connection.commit()
            print('Se añadio columna correctamente')
        except Exception:
            print('Error al añadir columna')
            print(Exception)

    def DropColumn(self, name_table, name_column):
        try:
            data = "alter table " + name_table + " drop column " + name_column
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print('Se añadio columna correctamente')
        except Exception:
            print('Error al añadir columna')
            print(ImportError.args)

    def RenameColumn(self, name_table, name_column, new_name):
        try:
            data = "alter table " + name_table + " rename column " + name_column + " to " + new_name
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print('Se añadio columna correctamente')
        except Exception:
            print('Error al añadir columna')

    def RenameTable(self, name_table, new_table):
        try:
            data = "alter table " + name_table + " rename to " +new_table
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print('Se añadio columna correctamente')
        except Exception:
            print('Error al añadir columna')

    def AddCheck(self, name_table, expression):
        try:
            data = "alter table " + name_table + " add check (" +expression+ ")"
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print('Se añadio columna correctamente')

        except Exception:
            print('Error al añadir columna')
