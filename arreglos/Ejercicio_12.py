
matriz = []

for f in range(5):
    fila = []
    for c in range(15):
        if f == 0 or f == 4 or c == 0 or c == 14:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(elemento, end="")
    print()