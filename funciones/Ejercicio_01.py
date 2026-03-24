# Procedimiento centrar: Recibe una cadena y la imprime centrada en la pantalla.
# Suponemos que tenemos una pantalla de 80 caracteres de ancho. 
# Para centrar usamos la formula 40 - (Longitud(cad)/2)
# Parámetros de entrada: cadena a imprimir centrada

def centrar(frase):
    message = " " * (40 - len(frase) // 2)
    message += frase
    print(message)
    message = " " * (40 - len(frase) // 2)
    message += '=' * len(frase)
    print(message)

if __name__ == "__main__":
    message_1 = input("Introduce una frase a centrar: ")
    message_2 = input("Introduce otra frase a centrar: ")
    print()
    centrar(message_1)
    centrar(message_2)