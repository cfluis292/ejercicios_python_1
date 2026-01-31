precio = float(input("Precio inicial por kilo: "))
kilos = float(input("Kilos vendidos: "))
tipo = input("Tipo (A/B): ").upper()
tamano = input("Tamaño (1/2): ")

if tipo == "A" and tamano == "1":
    precio += 0.20
elif tipo == "A" and tamano == "2":
    precio += 0.30
elif tipo == "B" and tamano == "1":
    precio -= 0.30
elif tipo == "B" and tamano == "2":
    precio -= 0.50

total = precio * kilos
print("Ganancia:", total)