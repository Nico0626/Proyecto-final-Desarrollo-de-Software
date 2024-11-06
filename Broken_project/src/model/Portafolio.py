
class Portafolio:
    def __init__(self, portafolio_id, usuario_id, total_invertido, saldo_cuenta, cantidad, valor, ganancia, simbolo):
        self.__portafolio_id = portafolio_id
        self.__usuario_id = usuario_id
        self.__total_invertido = total_invertido
        self.__saldo_cuenta = saldo_cuenta
        self.__cantidad = cantidad
        self.__valor = valor
        self.__ganancia = ganancia
        self.__simbolo = simbolo

    @property
    def portafolio_id(self):
        return self.__portafolio_id

    @property
    def usuario_id(self):
        return self.__usuario_id

    @property
    def total_invertido(self):
        return self.__total_invertido

    @property
    def saldo_cuenta(self):
        return self.__saldo_cuenta

    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def ganancia(self):
        return self.__ganancia   
    
    @property
    def simbolo(self):
        return self.__simbolo     

    def __repr__(self):
        return (f"Portafolio(portafolio_id={self.portafolio_id}, "
                f"usuario_id={self.usuario_id}, "
                f"total_invertido={self.total_invertido}," 
                f"saldo_cuenta={self.saldo_cuenta},"
                f"cantidad={self.cantidad},"
                f"valor={self.valor},"
                f"ganancia={self.ganancia},"
                f"simbolo={self.simbolo},"
                )
    