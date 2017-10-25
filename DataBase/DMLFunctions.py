from DataBase import Connection

class AdministrationData:

    connection = None

    def __init__(self):
        get_connection= Connection.DBConnection()
        self.connection = get_connection.returnInstance()

    def InsertData(self, name_table, values):
        try:
            data = "Insert into "+name_table+" values ("+values+")"
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
            print("Se insertaron los datos de manera exitosa")
        except:
            print("No se pudieron añadir los datos")

    def GetData(self, column_name, name_table):
        try:
           data= "\"\"Select "+column_name+" from "+name_table+"\"\""
           cursor = self.connection.cursor()
           cursor.execute(data)
           rows = cursor.fetchall()
           for row in rows:
               print (row)
        except:
            print("No se puede acceder a los datos")


    def UpdateData(self, table_name, column_name, new_value, condition):
        try:
            data = "Update "+table_name+" set "+column_name+" = "+new_value+" where "+column_name+" = "+condition
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
        except:
            print("No se pudo actualizar los datos")

    def DeleteData(self, name_table, column_name, expression):
        try:
            data="Delete from "+name_table+" where "+column_name+" = "+expression
            cursor = self.connection.cursor()
            cursor.execute(data)
            self.connection.commit()
        except:
            print("No se puede borrar los datos")

