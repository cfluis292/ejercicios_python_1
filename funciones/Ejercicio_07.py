

def login(nombre, password, intentos):
    if nombre == "luis" and password == "Cisneros123":
        return True, intentos
    else:
        intentos = intentos + 1
        return False, intentos

if __name__ == "__main__":
    
    intentos_actuales = 0
    
    
    usuario_ingresado = input("Escribe tu nombre de usuario: ")
    contrasena_ingresada = input("Escribe tu contraseña: ")
    acceso, intentos_actuales = login(usuario_ingresado, contrasena_ingresada, intentos_actuales)
    
    if acceso == True:
        print("ACCESO CORRECTO")
    else:
        print(f"Incorrecto ")