#Estructura de control If
#If else elif

'''
if exp_boleana:
	instrucciones

if exp_bool:
	instrucciones
elif exp_bool:
	instrucciones

'''

numero = int(input("Escribe un numero: "))

if numero > 0:
	print("Es un numero positivo")
elif numero == 0:
	print("El numero es 0")
else :
	print("Es un numero negativo")