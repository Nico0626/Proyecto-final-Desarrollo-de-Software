import sys
import os
from datetime import datetime
from decimal import Decimal
from src.dao.usuario_dao import UsuarioDAO
from src.model.Usuario import Usuario

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

def main():
    usuario_dao = UsuarioDAO()  # Crea una instancia de UsuarioDAO una vez

    while True:
        print("*** Menú Principal ***")
        print("1. Agregar Usuario")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            tipo = ""

            print("***Seleccione qué tipo de inversor***")
            print("1. Individual\n2. Empresa\n3. Institución\n")
            respuesta = input("Seleccione una opción: ")

            if respuesta == "1":
                tipo = "individual"
            elif respuesta == "2":
                tipo = "empresa"
            elif respuesta == "3":
                tipo = "institucion"
            else:
                print("Opción no válida. Intente de nuevo.")
                continue  # Regresa al inicio del bucle si la opción no es válida

            # Incluye la fecha de creación
            fecha_creacion = datetime.now()
            usuario = Usuario(usuario_id=None, nombre=nombre, apellido=apellido, tipo=tipo, saldo=Decimal('1000000.00'), fecha_creacion=fecha_creacion)

            try:
                # Crea el usuario en la base de datos
                usuario_dao.create(usuario)
                print("Usuario agregado exitosamente.")
            except Exception as e:
                print(f"Error al agregar usuario: {e}")

        elif opcion == "2":
            print("Saliendo del programa.")
            break  # Sale del bucle y termina el programa

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
