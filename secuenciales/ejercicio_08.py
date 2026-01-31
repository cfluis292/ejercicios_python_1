sueldo = float(input("Sueldo base: "))
v1 = float(input("Ingresa la venta 1: "))
v2 = float(input("Ingresa la venta 2: "))
v3 = float(input("Ingresa la venta 3: "))

comi = v1 * 0.1 + v2 * 0.1 + v3 * 0.1

print("Comisión por ventas: ", comi)
print("Sueldo total: ", sueldo + comi)