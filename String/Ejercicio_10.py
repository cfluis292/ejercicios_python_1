#Introducir cadena de caracteres e indicar s es un palindromo o no.

word = input("Ingresa una palabra: ")

if word == word[::-1]:
    print("La palabra es un palíndromo!")
else:
    print("La palabra no es un palíndromo!.")