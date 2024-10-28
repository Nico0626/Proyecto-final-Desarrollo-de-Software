# src/dao/PortafolioDAO.py
import mysql.connector
from src.model.Portafolio import Portafolio
from src.conn.Conexion import Conexiondb

class PortafolioDAO:
    def create(self, portafolio):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Portafolio (usuario_id, fecha_actualizacion) VALUES (%s, %s)"
            valores = (portafolio.usuario_id, portafolio.fecha_actualizacion)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Portafolio registrado.")
        except mysql.connector.Error as error:
            print("Error al crear portafolio:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, portafolio_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Portafolio WHERE portafolio_id = %s"
            cursor.execute(sql, (portafolio_id,))
            row = cursor.fetchone()
            if row:
                return Portafolio(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer portafolio:", error)
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

    def update(self, portafolio):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "UPDATE Portafolio SET usuario_id = %s, fecha_actualizacion = %s WHERE portafolio_id = %s"
            valores = (portafolio.usuario_id, portafolio.fecha_actualizacion, portafolio.portafolio_id)
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
