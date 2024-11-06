class Usuario:
    def __init__(self, usuario_id, nombre, apellido,documento,contraseña,mail, saldo, fecha_creacion):
        self.__usuario_id = usuario_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento= documento 
        self.__contraseña=contraseña
        self.__mail= mail
        self.__saldo = saldo
        self.__fecha_creacion = fecha_creacion 
        

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
    def documento(self):
       return self.__documento 
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    @property
    def mail(self):
        return self.__mail

    @property
    def saldo(self):
        return self.__saldo
  
    @property
    def fecha_creacion(self): 
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
        return f"({self.usuario_id}, '{self.nombre}', '{self.apellido}', '{self.documento}', {self.saldo}, {self.fecha_creacion})"