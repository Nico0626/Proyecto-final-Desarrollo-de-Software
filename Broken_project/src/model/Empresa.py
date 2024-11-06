class empresa:
    def __init__(self,empresa_id,nombre,cuit,sector,fecha_de_creacion):
        self.__empresa_id=empresa_id
        self.__nombre=nombre
        self.__cuit=cuit
        self.__sector=sector
        self.__fecha_de_creacion=fecha_de_creacion
         
    @property
    def empresa_id(self):
        return self.__empresa_id
    @property
    def nombre(self):
        return self.__nombre

    @property
    def cuit(self):
        self.__cuit

    @property
    def sector(self):
        return self.__sector
    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion
    

    @nombre.setter
    def cambiar_nombre(self,nuevo):
        self.__nombre=nuevo

    @sector.setter
    def sector(self, valor):
        self.__sector = valor

    def __repr__(self):
        return f"({self.empresa_id}, '{self.nombre}', '{self.cuit}', '{self.sector}', '{self.fecha_de_creacion}')"

