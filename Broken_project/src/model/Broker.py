import datetime

class Broker:
    def __init__(self, broker_id=None, nombre_broker=None, cuit=None, comision=None, fecha_creacion=None):
        self.__broker_id = broker_id
        self.__nombre_broker = nombre_broker
        self.__cuit = cuit
        self.__comision = comision
        self.__fecha_creacion = fecha_creacion or datetime.now()

    @property
    def broker_id(self):
        return self.__broker_id

    @property
    def nombre_broker(self):
        return self.__nombre_broker

    @nombre_broker.setter
    def nombre_broker(self, valor):
        self.__nombre_broker = valor

    @property
    def cuit(self):
        return self.__cuit

    @cuit.setter
    def cuit(self, valor):
        self.__cuit = valor

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, valor):
        self.__comision = valor

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    def __repr__(self):
        return f"({self.broker_id}, '{self.nombre_broker}', '{self.cuit}', {self.comision}, '{self.fecha_creacion}')"
