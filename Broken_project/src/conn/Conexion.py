import mysql.connector
from mysql.connector import Error

class Conexiondb:
    def __init__(self, host, user, password, database):
        self.host = 'localhost'
        self.user = 'root'
        self.password = "256323890" 
        self.database = 'broker'
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No hay conexión con la base de datos.")
            return None       
        cursor = self.connection.cursor(buffered=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)            
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()  
                return result
            self.connection.commit()
            print("Consulta ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            cursor.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            return"Conexión cerrada."    


conexion = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
