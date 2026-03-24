

matriz = []

for f in range(5):
    fila = []
    for c in range(5):
        fila.append(int(input(f"Fila {f+1}, Columna {c+1}: ")))
    matriz.append(fila)

print()
for f in range(5):
    print(f"Suma de la fila {f+1}: {sum(matriz[f])}")

print()
for c in range(5):
    suma_col = sum(matriz[f][c] for f in range(5))
    print(f"Suma de la columna {c+1}: {suma_col}")