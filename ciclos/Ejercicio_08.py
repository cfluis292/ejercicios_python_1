

inf = int(input("Límite inferior: "))
sup = int(input("Límite superior: "))

suma, fuera, limite = 0, 0, False

while True:
    n = int(input("Número (0 para salir): "))
    
    if n == 0: 
        break
        
    if inf < n < sup:
        suma += n
    else:
        fuera += 1
        if n == inf or n == sup:
            limite = True

print(f"\nSuma dentro: {suma}")
print(f"Cantidad fuera: {fuera}")
print(f"¿Tocó los límites?: {limite}")