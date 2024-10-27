import mysql.connector
from mysql.connector import Error

def conexion_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',  
            user='root',   
            password="256323890", 
            database='broker' 
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

def desconexion_bd(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión finalizada")

def registro_usuario(conexion):
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese nombre de usuario: ").strip()
    correo = input("Ingrese correo electrónico: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()

    cursor = conexion.cursor()
    consulta = "INSERT INTO inversor (nombre, correo, contraseña) VALUES (%s, %s, %s)"
    valores = (nombre, correo, contraseña)
    
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Usuario registrado exitosamente.")
    except Error as e:
        print(f"Error al registrar usuario: {e}")

def login(conexion):
    print("\n--- Inicio de Sesión ---")
    nombre = input("Ingrese nombre de usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()

    cursor = conexion.cursor()
    consulta = "SELECT id, contraseña, intentos_fallidos, bloqueado FROM inversor WHERE nombre = %s"
    cursor.execute(consulta, (nombre,))
    inversor = cursor.fetchone()

    if inversor:
        user_id, stored_password, intentos_fallidos, bloqueado = inversor

        if bloqueado:
            print("Tu cuenta está bloqueada debido a intentos fallidos.")
            return

        if contraseña == stored_password:
            print(f"Bienvenido {nombre}, has iniciado sesión correctamente.")
            
            cursor.execute("UPDATE inversor SET intentos_fallidos = 0 WHERE id = %s", (user_id,))
            conexion.commit()
        else:
            intentos_fallidos += 1
            if intentos_fallidos >= 3:
                cursor.execute("UPDATE inversor SET intentos_fallidos = %s, bloqueado = TRUE WHERE id = %s", 
                               (intentos_fallidos, user_id))
                print("Has alcanzado el límite de intentos. Cuenta bloqueada.")
            else:
                cursor.execute("UPDATE inversor SET intentos_fallidos = %s WHERE id = %s", 
                               (intentos_fallidos, user_id))
                print(f"Contraseña incorrecta. Intentos fallidos: {intentos_fallidos}/3.")
            conexion.commit()
    else:
        print("El nombre de usuario no existe.")

def desbloquear_cuenta(conexion):
    print("\n--- Desbloquear Cuenta ---")
    nombre = input("Ingresa tu nombre de usuario: ").strip()
    correo = input("Ingresa tu correo electrónico registrado: ").strip()

    cursor = conexion.cursor()
    consulta = "SELECT id, bloqueado FROM inversor WHERE nombre = %s AND correo = %s"
    cursor.execute(consulta, (nombre, correo))
    inversor = cursor.fetchone()

    if inversor:
        user_id, bloqueado = inversor
        if bloqueado:
            cursor.execute("UPDATE inversor SET intentos_fallidos = 0, bloqueado = FALSE WHERE id = %s", (user_id,))
            conexion.commit()
            print("Tu cuenta ha sido desbloqueada exitosamente.")
        else:
            print("La cuenta no está bloqueada.")
    else:
        print("Error: El nombre de usuario o correo no coinciden.")


def recuperar_contraseña(conexion):
    print("\n--- Recuperar Contraseña ---")
    nombre = input("Ingrese nombre de usuario: ").strip()
    correo = input("Ingrese correo electrónico registrado: ").strip()

    cursor = conexion.cursor()
    consulta = "SELECT contraseña FROM inversor WHERE nombre = %s AND correo = %s"
    valores = (nombre, correo)

    try:
        cursor.execute(consulta, valores)
        resultado = cursor.fetchone()
        if resultado:
            print(f"Tu contraseña es: {resultado[0]}")
        else:
            print("Error: El nombre de usuario o correo no coinciden.")
    except Error as e:
        print(f"Error al recuperar la contraseña: {e}")
        
def mostrar_menu():
    print("--- Menú ---")
    print("1. Registro")
    print("2. Inicio de Sesión")
    print("3. Recuperar Contraseña")
    print("4. Desbloquear Cuenta")
    print("5. Salir")

def iniciar_programa():
    conexion = conexion_bd()
    if conexion:
        while True:
            mostrar_menu()
            opcion = input("Selecciona una opción: ").strip()
            if opcion == '1':
                registro_usuario(conexion)
            elif opcion == '2':
                login(conexion)
            elif opcion == '3':
                recuperar_contraseña(conexion)
            elif opcion == '4':
                desbloquear_cuenta(conexion)
            elif opcion == '5':
                print("Saliendo del programa.")
                desconexion_bd(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    iniciar_programa()



