character = input('Escribe una letra (" " para salir)')

while character != " ":
    if len(character) == 1:
        if character.upper() == 'A' \
           or character.upper() == 'E' \
           or character.upper() == 'I' \
           or character.upper() == 'O' \
           or character.upper() == 'U':
            print("Es una vocal")
        else:
            print("No es una vocal")
    else:
        print("Solo puedes introducir una letra")
    character = input('Escribe una letra (" " para salir)')
