

matriz = []

for f in range(5):
    fila = []
    for c in range(5):
        if f == c or f == 4 - c:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()