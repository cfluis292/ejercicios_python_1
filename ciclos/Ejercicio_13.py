

if __name__ == "__main__":
    print("Calculadora de Sueldo Semanal")
    
    sueldo_por_hora = float(input("Introduce el sueldo por hora: $"))
    
    
    horas_acum = 0
    

    for dia in range(1, 7):
        horas = int(input(f"¿Cuántas horas has trabajado el día {dia}?: "))
        horas_acum += horas

    sueldo_semanal = horas_acum * sueldo_por_hora
    print(f"Sueldo semanal: ${sueldo_semanal}")