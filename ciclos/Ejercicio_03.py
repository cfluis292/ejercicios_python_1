suma = 0
cont = 0

print("Número (0 para salir):")
num = int(input())

while num != 0:
    suma = suma + num
    cont = cont + 1
    print("Número (0 para salir):")
    num = int(input())

if cont > 0:
    media = suma / cont
    print("La suma total es:", suma)
    print("La media es:", media)
else:
    print("No se ingresaron números.")
