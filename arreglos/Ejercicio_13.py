


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombres = []
kms = []

while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    if num_conductores <= 10:
        break
    print("Como máximo puedo guardar la información de 10 conductores.")

for i in range(num_conductores):
    nombres.append(input(f"Nombre del conductor {i+1}: "))
    
    kms_diarios = []
    for dia in dias:
        kms_diarios.append(int(input(f"¿Cuántos km ha realizado el {dia}?: ")))
        
    kms_diarios.append(sum(kms_diarios))
    kms.append(kms_diarios)

for i in range(num_conductores):
    print(f"{nombres[i]} ha realizado {kms[i][7]} kms.")