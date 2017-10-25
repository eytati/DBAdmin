import psycopg2

class DBConnection:
    instance = None
    connection = None

    def ConnectionRemote(self, name, user, password):
        if not self.instance:
            host = 'localhost'
            connection_string = 'host=' + '\'' + host + '\'' + 'dbname=' + '\'' + name + '\'' + 'user=' + '\'' + user + '\'' + 'password=' + '\'' + password + '\''
            try:
                self.connection = psycopg2.connect(connection_string)
                print("Conexion exitosa")
            except Exception:
                print('Datos ingresados erroneos')

    def ConnectionLocal(self, name, user, password):
        if not self.instance:
            host = 'localhost'
            connection_string = 'host=' + '\'' + host + '\'' + 'dbname=' + '\'' + name + '\'' + 'user=' + '\'' + user + '\'' + 'password=' + '\'' + password + '\''
            try:
                self.connection = psycopg2.connect(connection_string)
                print("Conexion exitosa")
            except Exception:
                print('Datos ingresados erroneos')

    def closeConnection(self):
        try:
            self.connection.close()
            self.connection = None
        except Exception:
            print('No se cerro la conexion')
            print(Exception)

    def returnInstance(self):
        return self.connection