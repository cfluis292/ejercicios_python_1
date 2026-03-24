

precios = []
cantidades = []

for i in range(5):
    precios.append(float(input(f"Ingrese Precio Articulo {i+1}: ")))

for i in range(4):
    sucursal = []
    for j in range(5):
        sucursal.append(float(input(f"Ingresa la cantidad de articulos {j+1}, en sucursal {i+1}: ")))
    cantidades.append(sucursal)

print("Cantidades por artículos:")
for j in range(5):
    suma = sum(cantidades[i][j] for i in range(4))
    print("Total articulo {j+1}: {suma}")

articulos_sucursal2 = sum(cantidades[1])
print("Total Sucursal 2: {articulos_sucursal2}")

print("Sucursal 1, Articulo 3: {cantidades[0][2]}\n")

mayor_rec = 0
num_mayor = 0
total_empresa = 0

for i in range(4):
    total_sucursal = sum(cantidades[i][j] * precios[j] for j in range(5))
    print(f"Recaudaciones Sucursal {i+1}: {total_sucursal}")
    
    if total_sucursal > mayor_rec:
        mayor_rec = total_sucursal
        num_mayor = i + 1
        
    total_empresa += total_sucursal

print(f"\nRecaudación total de la empresa: {total_empresa}")
print(f"Sucursal de Mayor Recaudación: {num_mayor}")