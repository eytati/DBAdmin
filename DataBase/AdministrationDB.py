import  psycopg2

class DBConnection:
    instance = None
    connection = None

    def __init__(self):
        if not self.instance:
            self.con = psycopg2.connect("host='localhost' dbname='Prueba' user='postgres' password='hola'")

    def returnInstance(self):
        return self.con

class AdministrationData:

    connection = None

    def GetConnection(self):
        get_connection: DBConnection()
        self.connection = get_connection.returnInstance()

    def InsertData(self, **kwargs):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO hola VALUES ('asd', 'asdf')")
        self.connection.commit()

    def GetData(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * from hola""")
        rows = cursor.fetchall()
        for row in rows:
            print (row[0])

class AdministrationDB:

    connection: None

    def GetConnection(self):
        get_connection: DBConnection()
        self.connection = get_connection.returnInstance()

    def CreateDB(self):
        return

    def GetDB(self):
        return

    def UpdateDB(self):
        return

    def DeleteDB(self):
        return

class AdministrationTables:

    connection = None

    def GetConnection(self):
        get_connection: DBConnection()
        self.connection = get_connection.returnInstance()

    def CreateTables(self):
        cursor = self.connection.cursor()
        cursor.execute("Create table hola2(prueba1 VARCHAR (50), prueba2 DECIMAL (5))")
        self.connection.commit()

    def GetTables(self):
        return

    def UpdateTables(self):
        return

    def DeleteTables(self):
        return

class AdministrationData:

    connection = None

    def GetConnection(self):
        get_connection: DBConnection()
        self.connection = get_connection.returnInstance()

    def InsertData(self, **kwargs):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO hola VALUES ('asd', 'asdf')")
        self.connection.commit()

    def GetData(self):
        cursor = self.connection.cursor()
        cursor.execute("""SELECT * from hola""")
        rows = cursor.fetchall()
        for row in rows:
            print (row[0])


    def UpdateData(self):
        return

    def DeleteData(self):
        return