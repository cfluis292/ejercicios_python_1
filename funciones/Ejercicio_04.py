# ################################################################################
# Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra 
# con los mismos caracteres separados con espacio.
# Parámetros de entrada: Cadena de caracteres
# Dato devuelto: Cadena igual a la anterior pero con espacios entre los 
# caracteres
# ################################################################################

def convertir_espaciado(cad):
    cad_con_espacios = ""
    for caracter in cad:
        # Concateno el carácter y un espacio
        cad_con_espacios += caracter + " "
    return cad_con_espacios

# ################################################################################
# Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y 
# devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
# "Hola, tú" devolverá "H o l a , t ú ". Crea un programa principal donde se 
# use dicha función.
# ################################################################################

def principal():
    # El parámetro 'end=""' en input hace el equivalente a 'Sin Saltar'
    mensaje = input("Introduce una cadena: ")
    print("La cadena con espacio:")
    print(convertir_espaciado(mensaje))

# Punto de entrada del programa
if __name__ == "__main__":
    principal()