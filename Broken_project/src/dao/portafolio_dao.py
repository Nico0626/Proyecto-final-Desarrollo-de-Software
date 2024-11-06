import mysql.connector
from model.Portafolio import Portafolio
from conn.Conexion import Conexiondb

class PortafolioDAO:
    def create(self, usuario_id, simbolo, cantidad):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Portafolio (usuario_id, simbolo, cantidad) VALUES (%s, %s,%s)"
            valores = (usuario_id, simbolo, cantidad)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Portafolio registrado con exito.")
        except mysql.connector.Error as error:
            print("Error al crear portafolio:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, usuario_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Portafolio WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            rows = cursor.fetchall()
            if rows:
                return[Portafolio(*row) for row in rows]
            return []
        except mysql.connector.Error as error:
            print("Error al leer portafolio:", error)
            return []
        finally:
            cursor.close()
            cone.close()

    def read_by_simbolo(self, usuario_id, simbolo):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Portafolio WHERE usuario_id = %s AND simbolo = %s"
            cursor.execute(sql, (usuario_id, simbolo))
            row = cursor.fetchone()
            if row:
                return Portafolio(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer portafolio por símbolo:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Portafolio"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Portafolio(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todos los portafolios:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, usuario_id, simbolo, cantidad):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "UPDATE Portafolio SET cantidad = cantidad + %s WHERE usuario_id = %s AND simbolo = %s"
            valores = (cantidad, usuario_id, simbolo)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Portafolio actualizado.")
        except mysql.connector.Error as error:
            print("Error al actualizar portafolio:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, portafolio_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Portafolio WHERE portafolio_id = %s"
            cursor.execute(sql, (portafolio_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Portafolio eliminado.")
        except mysql.connector.Error as error:
            print("Error al eliminar portafolio:", error)
        finally:
            cursor.close()
            cone.close()

    def get_portafolio_id(self, usuario_id, simbolo):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT portafolio_id FROM Portafolio WHERE usuario_id = %s AND simbolo = %s"
            cursor.execute(sql, (usuario_id, simbolo))
            portafolio_id = cursor.fetchone()

            if portafolio_id:
                return portafolio_id[0]
            else:
                print("No se encontró el portafolio.")
                return None

        except mysql.connector.Error as error:
            print("Error al obtener portafolio_id:", error)
            return None
        finally:
            cursor.close()
            cone.close()
