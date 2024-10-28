
class Portafolio:
    def __init__(self, portafolio_id, usuario_id, fecha_actualizacion):
        self.__portafolio_id = portafolio_id
        self.__usuario_id = usuario_id
        self.__fecha_actualizacion = fecha_actualizacion

    @property
    def portafolio_id(self):
        return self.__portafolio_id

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def fecha_actualizacion(self):
        return self.__fecha_actualizacion

    @fecha_actualizacion.setter
    def fecha_actualizacion(self, valor):
        self.__fecha_actualizacion = valor

    def __repr__(self):
        return (f"Portafolio(portafolio_id={self.portafolio_id}, "
                f"usuario_id={self.usuario_id}, "
                f"fecha_actualizacion={self.fecha_actualizacion})")
    