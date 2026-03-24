
def esbisiesto(year):
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    
    usuario = int(input("Introduce el año que quieres revisar: "))
    resultado = esbisiesto(usuario)
    
    if resultado == True:
        print(f"¡El año {usuario} Febrero tiene 29 días.")
    else:
        print(f"El año {usuario} No es bisiesto. Febrero solo tiene 28 días.")