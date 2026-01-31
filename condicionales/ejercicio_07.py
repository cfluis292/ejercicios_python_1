base = int(input("Ingrea la base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente > 0:
    potencia = base ** exponente
    print("La potencia es", potencia)
elif exponente == 0:
    print("La potencia es 1")
else:
    potencia = base ** abs(exponente)
    resultado = 1 / potencia
    print("La potencia es", resultado)