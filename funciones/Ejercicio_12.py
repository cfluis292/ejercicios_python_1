

def dias_del_mes(month, year):

    if month == 2:
        return 28

    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def validar_fecha(day, month, year):
    if day < 1 or day > dias_del_mes(month, year):
        return False
    else:
        return True

if __name__ == "__main__":
    
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes (1-12): "))
    anio = int(input("Introduce el año: "))
    fecha_correcta = validar_fecha(dia, mes, anio)
    
    if fecha_correcta == True:
        print("¡Todo en orden! Es una fecha válida del calendario.")
    else:
        print("Error! Esa fecha no existe. Revisa el día o el mes.") 