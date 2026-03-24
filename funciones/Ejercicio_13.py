
def ordn(n1, n2):
    el_mayor = max(n1, n2)
    el_menor = min(n1, n2)
    return el_mayor, el_menor

a = int(input("Escribe un número: "))
b = int(input("Escribe otro: "))

grande, pequeño = ordn(a, b)

print("-" * 30)
print(f"El más grande es el {grande}")
print(f"El más pequeño es el {pequeño}")
print("-" * 30)