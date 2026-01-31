peso = int(input("Peso (gramos): "))

if peso < 1 or peso > 5000:
    print("Peso no válido")
else:
    zona = int(input("Zona (1-5): "))
    
    if zona == 1:
        costo = peso * 24
    elif zona == 2:
        costo = peso * 20
    elif zona == 3:
        costo = peso * 21
    elif zona == 4:
        costo = peso * 10
    elif zona == 5:
        costo = peso * 18
    else:
        print("Zona no válida")
        costo = 0
    
    if costo > 0:
        print("Costo:", costo / 1000)