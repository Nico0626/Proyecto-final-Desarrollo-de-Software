# src/dao/BrokerDAO.py
import mysql.connector
from model.Broker import Broker
from conn.Conexion import Conexiondb

class BrokerDAO:
    def create(self, broker):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Broker (nombre_broker, cuit, comision) VALUES (%s, %s, %s)"
            valores = (broker.nombre_broker, broker.cuit, broker.comision)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Broker registrado.")
        except mysql.connector.Error as error:
            print("Error al crear broker:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, broker_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Broker WHERE broker_id = %s"
            cursor.execute(sql, (broker_id,))
            row = cursor.fetchone()
            if row:
                return Broker(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer broker:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Broker"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Broker(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todos los brokers:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, broker):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "UPDATE Broker SET nombre_broker = %s, cuit = %s, comision = %s WHERE broker_id = %s"
            valores = (broker.nombre_broker, broker.cuit, broker.comision, broker.broker_id)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Broker actualizado.")
        except mysql.connector.Error as error:
            print("Error al actualizar broker:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, broker_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Broker WHERE broker_id = %s"
            cursor.execute(sql, (broker_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Broker eliminado.")
        except mysql.connector.Error as error:
            print("Error al eliminar broker:", error)
        finally:
            cursor.close()
            cone.close()
