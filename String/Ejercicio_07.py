#Pide una cadena y dos caracteres por teclado.
#Sustituye en la cadena todas las apariciones del primer carácter por el segundo carácter e imprímela.

frase = input("Ingrese una frase: ")

while True:
    letra_1 = input("Ingresa una letra: ")
    if len(letra_1) == 1:
        break

while True:
    letra_2 = input("Ingresa una letra para sustituir la primera: ")
    if len(letra_2) == 1:
        break

frase_nueva = ""
for letra in frase:
    if letra == letra_1:
        frase_nueva = frase_nueva + letra_2
    else:
        frase_nueva += letra

print("La frase nueva queda así:\n" + frase_nueva)

frase_2 = frase.replace(letra_1, letra_2)
print("La frase nueva queda así:\n" + frase_2)