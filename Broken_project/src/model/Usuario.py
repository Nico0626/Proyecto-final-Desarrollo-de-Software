
class Usuario:
    def __init__(self, usuario_id, nombre, apellido, tipo, saldo, fecha_creacion):
        self.__usuario_id = usuario_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipo = tipo
        self.__saldo = saldo
        self.__fecha_creacion = fecha_creacion

        @property

        @property

        @property

        @property

        @property




      def registro():
        nombre=input("Ingrese su nombre ")
        apellido=input("Ingrese su apellido")
        usuario_id=input("Ingrese su nombre de usuario")
        tipo=""
        while True:
            respuesta=int(input("""---Ingrese el numero que corresponda a su respuesta---\n
                            Usted es:\n 
                            1.Persona individual \n 
                            2.Empresa \n
                            3.Institucion """))
            if respuesta!=1 or 2 or 3:
                print("ERROR:ingrese un valor valido")
                return False 
        if respuesta==1:
            tipo="individual"
        elif respuesta==2:
            tipo="empresa"
        elif respuesta==3:
            tipo="institucion"  