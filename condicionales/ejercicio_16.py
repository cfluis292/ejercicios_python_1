tiempo = int(input("Tiempo de llamada en minutos): "))
domingo = input("¿Es domingo? (S/N): ").upper()

coste = 0

if tiempo <= 5:
    coste = tiempo * 100
elif tiempo <= 8:
    coste = 500 + (tiempo - 5) * 80
elif tiempo <= 10:
    coste = 500 + 240 + (tiempo - 8) * 70
else:
    coste = 500 + 240 + 140 + (tiempo - 10) * 50

if domingo == "S":
    coste += coste * 0.03
else:
    turno = input("¿Turno? (m/t): ").upper()
    if turno == "M":
        coste += coste * 0.15
    else:
        coste += coste * 0.10

print("Costo:", coste/100)