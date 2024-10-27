class Usuario:
    def __init__(self, usuario_id, nombre, apellido,contraseña,gmail, tipo, saldo, fecha_creacion):
        self.__usuario_id = usuario_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contraseña=contraseña
        self.__gmail=gmail
        self.__tipo = tipo
        self.__saldo = saldo
        self.__fecha_creacion = fecha_creacion  # Cambiado para que sea privado

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    @property
    def gmail(self):
        return self.__gmail

    @property
    def tipo(self):
        return self.__tipo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def fecha_creacion(self):  # Agregado para acceder a fecha_creacion
        return self.__fecha_creacion

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def __repr__(self):
        return f"({self.usuario_id}, '{self.nombre}', '{self.apellido}', '{self.tipo}', {self.saldo}, {self.fecha_creacion})"