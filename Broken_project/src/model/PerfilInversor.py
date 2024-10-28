class PerfilInversor:
    def __init__(self, perfil_id=None, usuario_id=None, tolerancia_riesgo="", duracion_inversion=""):
        self.__perfil_id = perfil_id
        self.__usuario_id = usuario_id
        self.__tolerancia_riesgo = tolerancia_riesgo
        self.__duracion_inversion = duracion_inversion

    @property
    def perfil_id(self):
        return self.__perfil_id

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def tolerancia_riesgo(self):
        return self.__tolerancia_riesgo

    @tolerancia_riesgo.setter
    def tolerancia_riesgo(self, valor):
        self.__tolerancia_riesgo = valor

    @property
    def duracion_inversion(self):
        return self.__duracion_inversion

    @duracion_inversion.setter
    def duracion_inversion(self, valor):
        self.__duracion_inversion = valor

    def __repr__(self):
        return f"({self.perfil_id}, {self.usuario_id}, '{self.tolerancia_riesgo}', '{self.duracion_inversion}')"
