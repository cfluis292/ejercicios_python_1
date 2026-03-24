# Programa que calcula el factorial de un número
# Con ciclo while

num = int(input('Ingresa un número: '))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print('El factorial de', num, 'es', factorial)