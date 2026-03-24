
def calcular_factorial(num):
    if num == 1 or num == 0: 
        return 1
    else:
        return num * calcular_factorial(num - 1)

if __name__ == "__main__":
    print("Calculadora de Factoriales")
    
    numero_usuario = int(input("Introduce un número: "))
    resultado = calcular_factorial(numero_usuario)
    
    print(f"El factorial de {numero_usuario} es: {resultado}") 