# src/dao/TransaccionDAO.py
import mysql.connector
from src.model.Transaccion import Transaccion
from src.conn.Conexion import Conexiondb

class TransaccionDAO:
    def create(self, transaccion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                INSERT INTO Transacciones (usuario_id, accion_id, broker_id, tipo, cantidad, precio, comision, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                transaccion.usuario_id,
                transaccion.accion_id,
                transaccion.broker_id,
                transaccion.tipo,
                transaccion.cantidad,
                transaccion.precio,
                transaccion.comision,
                transaccion.fecha
            )
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Transacción registrada.")
        except mysql.connector.Error as error:
            print("Error al crear transacción:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, transaccion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Transacciones WHERE transaccion_id = %s"
            cursor.execute(sql, (transaccion_id,))
            row = cursor.fetchone()
            if row:
                return Transaccion(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer transacción:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Transacciones"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Transaccion(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todas las transacciones:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, transaccion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE Transacciones 
                SET usuario_id = %s, accion_id = %s, broker_id = %s, tipo = %s, cantidad = %s, precio = %s, comision = %s, fecha = %s
                WHERE transaccion_id = %s
            """
            valores = (
                transaccion.usuario_id,
                transaccion.accion_id,
                transaccion.broker_id,
                transaccion.tipo,
                transaccion.cantidad,
                transaccion.precio,
                transaccion.comision,
                transaccion.fecha,
                transaccion.transaccion_id
            )
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Transacción actualizada.")
        except mysql.connector.Error as error:
            print("Error al actualizar transacción:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, transaccion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Transacciones WHERE transaccion_id = %s"
            cursor.execute(sql, (transaccion_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Transacción eliminada.")
        except mysql.connector.Error as error:
            print("Error al eliminar transacción:", error)
        finally:
            cursor.close()
            cone.close()
