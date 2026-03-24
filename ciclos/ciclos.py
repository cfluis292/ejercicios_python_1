print("Range con un parametro")
for i in range(5):
    print(i)

print("\nRange con 2 parametros") 
for i in range(2, 5):
    print(i)

print("\nRange con 3 parametros")
for i in range(1, 10, 2):
    print(i)
print()

message = "Los dormidos puntos menos"
for letra in message:
    print(letra, end="-")
print("\n")


i = 1
while i <= 5:
    print(f"Iteración del while principal: {i}")
    i = i + 1

    user_input = input("Escribe 'Salir' para continuar: ")
    while user_input != "Salir":
        user_input = input("Dije que escribas 'Salir': ")