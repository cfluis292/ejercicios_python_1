

print("PAGO DE SALARIOS")

empleados = int(input("Cantidad de empleados: "))
tarifa_hora = float(input("Pago por hora: "))

horas_totales = 0

for i in range(1, empleados + 1):
    horas_empleado = 0
    jornadas = int(input(f"Días laborados por el empleado {i}: "))
    
    for j in range(1, jornadas + 1):
        horas_empleado += int(input(f"Horas del día {j}: "))
        
    salario = horas_empleado * tarifa_hora
    print(f"Salario del empleado {i}: ${salario}")
    
    horas_totales += horas_empleado

print(f"Total a pagar por la empresa: ${horas_totales * tarifa_hora}")