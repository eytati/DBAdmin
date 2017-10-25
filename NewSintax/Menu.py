from DataBase import Connection, DDLFuntions, DMLFunctions, AdministrationDB
import getpass
import os
print("Bienvenido")

class Started:

    def InputInformation(self, argument):
        value = input(argument)
        return value


    def DbConnection(self):
        argument = "Escogé una accion ingresando el número \n1.Conectarse a Base Datos \n2.Exit\n"
        choose = self.InputInformation(argument)
        if (choose == '1'):
            db_name = self.InputInformation("Ingrese nombre de la base de datos que desea acceder: ")
            user_name= self.InputInformation("Ingrese usuario de la base de datos que desea acceder: ")
            user_password = self.InputInformation("Ingrese contrase del usuario anterior: ")
            connection = Connection.DBConnection()
            connection.ConnectionLocal(db_name, user_name, user_password)
            os.system('cls' if os.name=='nt' else 'clear')
            self.GeneralMenu()
        else:
            print("Gracias")


    def GeneralMenu(self):
        connection = Connection.DBConnection()
        argument = "Escogé una accion ingresando el número \n1.Conectarse a otra base de datos \n2.Usuarios \n3.DDL\n4.DML\n5.Cambios en la base de datos\n6.Salir"
        choose = self.InputInformation(argument)
        if(choose=='1'):
            connection.closeConnection()
            self.DbConnection()
        elif (choose == '2'):
            return
        elif (choose == '3'):
            return self.DDLMenu()
        elif (choose == '4'):
            return self.DMLMenu()
        elif (choose == '5'):
            return self.DbChanges()
        elif (choose == '6'):
            connection.closeConnection()
            print("Gracias")
        else:
            return self.GeneralMenu()


    def UserMenu(self):
        argument = ""
        choose = self.InputInformation(argument)


    def DDLMenu(self):
        argument = "Escogé una accion ingresando el número \n1.Crear tablar \n2.Ver tablas \n3.Eliminar tablas\n4.Editar tablas\n5.Volver a menu principal"
        choose = self.InputInformation(argument)
        ddl_functions = DDLFuntions.AdministrationTables()

        if (choose == '1'):
            table_name = self.InputInformation("Ingrese nombre de la tabla")
            create_table = self.InputInformation("Ingrese nombre y tipo de cada columna que desea crear \nEjemplo: columna_ejemplo varchar(10)")
            return ddl_functions.CreateTables(table_name, create_table)

        elif (choose == '2'):
            table_name = self.InputInformation("Nombre de tabla que desea ver")
            return ddl_functions.GetTables(table_name)

        elif (choose == '3'):
            table_name = self.InputInformation("Nombre de tabla que desea eliminar")
            return ddl_functions.DeleteTables(table_name)

        elif (choose == '4'):
            return self.AlterTablesDLLMenu()

        elif (choose == '5'):
            return self.GeneralMenu()

        else:
            return self.DDLMenu()


    def AlterTablesDLLMenu(self):
        argument = "Escogé una accion ingresando el número \n1.Añadir columna \n2.Eliminar columna \n3.Renombrar columna\n4.Renombrar tabla\n5.Añadir check\n6.Volver a menu"
        choose = self.InputInformation(argument)
        ddl_functions = DDLFuntions.UpdateTables()

        if (choose == '1'):
            name_table = self.InputInformation('Nombre de la tabla')
            name_column = self.InputInformation('Nombre de la columna')
            type = self.InputInformation('Tipo de dato')
            ddl_functions.AddColumn(name_table, name_column, type)
            return self.AlterTablesDLLMenu()


        elif (choose == '2'):
            name_table = self.InputInformation('Nombre de la tabla')
            name_column = self.InputInformation('Nombre de la columna')
            ddl_functions.DropColumn(name_table, name_column)
            return self.AlterTablesDLLMenu()


        elif (choose == '3'):
            name_table = self.InputInformation('Nombre de la tabla')
            name_column = self.InputInformation('Nombre de la columna')
            new_name= self.InputInformation('El nuevo nombre')
            ddl_functions.RenameColumn(name_table, name_column, new_name)
            return self.AlterTablesDLLMenu()


        elif (choose == '4'):
            name_table = self.InputInformation('Nombre de la tabla')
            new_name = self.InputInformation('El nuevo nombre')
            ddl_functions.RenameTable(name_table, new_name)
            return self.AlterTablesDLLMenu()


        elif (choose == '5'):
            name_table = self.InputInformation('Nombre de la tabla')
            expression = self.InputInformation('Expresion con la cual se hace efectivo el check')
            ddl_functions.AddCheck(name_table, expression)
            return self.AlterTablesDLLMenu()

        elif(choose  == '6'):
            return self.DDLMenu()

        else:
            return self.AlterTablesDLLMenu()


    def DMLMenu(self):
        dml_functions = DMLFunctions.AdministrationData()
        argument = "Escogé una accion ingresando el número \n1.Insertar datos \n2.Ver los datos \n3.Actualizar datos \n4.Eliminar datos\n5.Volver a menu"
        choose = self.InputInformation(argument)

        if (choose == '1'):
            name_table = self.InputInformation("Ingrese el nombre la tabla a la cual desea añadir datos")
            values = self.InputInformation("Ingrese los datos en el orden respectivo y separados por coma ','")
            dml_functions.InsertData(name_table, values)
            return self.DMLMenu()

        elif (choose == '2'):
            column_name = self.InputInformation("Ingrese los nombres de las columnas que desea ver separado por coma ',")
            name_table =self.InputInformation("Ingrese el nombre de la tabla")
            dml_functions.GetData(column_name, name_table)
            return self.DMLMenu()

        elif (choose == '3'):
            name_table = self.InputInformation("Ingrese el nombre de la tabla")
            column_name = self.InputInformation("Ingrese los nombres de las columnas que desea editar")
            new_value = self.InputInformation("Ingrese nuevo valor")
            condition= self.InputInformation("Ingresar el identificador del elemento o elementos que desea cambiar")
            dml_functions.UpdateData(name_table, column_name, new_value, condition)
            return self.DMLMenu()

        elif (choose == '4'):
            name_table = self.InputInformation("Ingrese el nombre de la tabla")
            column_name = self.InputInformation("Ingrese los nombres de las columnas que desea editar")
            condition = self.InputInformation("Ingresar el identificador del elemento o elementos que desea cambiar")
            dml_functions.DeleteData(name_table, column_name, condition)
            return self.DMLMenu()

        elif (choose == '5'):
            return  self.DMLMenu()

        else:
            return self.GeneralMenu()

    def DbChanges(self):
        changes = AdministrationDB.AdministrationDB()
        argument = "Escogé una accion ingresando el número \n1.Crear base de datos \n2.Ver todas las tablas de la base de datos\n3.Actualizar la base de datos\n4.Eliminar Base de datos\n5.Volver a menu"
        choose = self.InputInformation(argument)
        if (choose == '1'):
            db_name = self.InputInformation("Ingrese el nombre de la base de datos")
            owner = self.InputInformation("Ingrese el usuario propetario")
            template = self.InputInformation("Ingrese el template")
            encoding = self.InputInformation("Ingrese el encoding")
            collate = 'C'
            type = 'C'
            table_space = 'pg_default'
            connection = self.InputInformation("Ingrese el nombre de la tabla")
            changes.CreateDB(db_name, owner, template, encoding, collate, type, table_space, connection)
            return self.DbChanges()

        elif (choose == '2'):
            changes.GetDB()
            return self.DbChanges()

        elif (choose == '3'):
            self.AlterDB()
            return self.DbChanges()

        elif (choose == '4'):
            db_name = self.InputInformation("Ingrese el nombre de la base de datos")
            changes.DeleteDB(db_name)
            return self.DbChanges()

        elif (choose == '5'):
            return self.GeneralMenu()

        else:
            return self.DbChanges()

    def AlterDB(self):
        update_db = AdministrationDB.UpdateDataBase()
        argument = "Escogé una accion ingresando el número \n1.Renombrar base de datos \n2.Cambiar el usuario dueño de la base \n3.Cambiar cantidad de conexiones \n4.Volver a menu"
        choose = self.InputInformation(argument)
        if(choose):
            db_name = self.InputInformation("Ingrese el nombre de la base de datos")
            new_name = self.InputInformation("Ingrese el nuevo nombre de la base de datos")
            update_db.RenameDB(db_name,new_name)
            return self.AlterDB()

        elif (choose == '2'):
            db_name = self.InputInformation("Ingrese el nombre de la base de datos")
            new_owner = self.InputInformation("Nuevo usuario")
            update_db.ChangeOwner(db_name,new_owner)
            return self.AlterDB()

        elif (choose == '3'):
            db_name = self.InputInformation("Ingrese el nombre de la base de datos")
            connections = self.InputInformation("Numero de conexiones")
            update_db.ChangeConnections(db_name, connections)
            return self.AlterDB()

        elif (choose == '4'):
            return self.GeneralMenu()

        else:
            return self.AlterDB()

a = Started()
a.DbConnection()