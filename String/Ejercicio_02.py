#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
cadena = input("Escribe Algo: ")
subcadena = input("Escribe una subcadena: ")

if cadena.startswith(subcadena):
    print(cadena, "Si comienza con", subcadena)
else:
    print(cadena, "No comienza con", subcadena)