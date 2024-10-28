import datetime
from decimal import Decimal

class Transaccion:
    def __init__(self, transaccion_id=None, usuario_id=None, accion_id=None, broker_id=None, tipo="", cantidad=0, precio=Decimal('0.00'), comision=Decimal('0.00'), fecha=None):
        self.__transaccion_id = transaccion_id
        self.__usuario_id = usuario_id
        self.__accion_id = accion_id
        self.__broker_id = broker_id
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__precio = precio
        self.__comision = comision
        self.__fecha = fecha if fecha is not None else datetime.now()

    @property
    def transaccion_id(self):
        return self.__transaccion_id

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def accion_id(self):
        return self.__accion_id

    @property
    def broker_id(self):
        return self.__broker_id

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio(self):
        return self.__precio

    @property
    def comision(self):
        return self.__comision

    @property
    def fecha(self):
        return self.__fecha

    def __repr__(self):
        return f"({self.transaccion_id}, {self.usuario_id}, {self.accion_id}, {self.broker_id}, '{self.tipo}', {self.cantidad}, {self.precio}, {self.comision}, '{self.fecha}')"
