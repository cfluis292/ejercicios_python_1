

if __name__ == "__main__":
    print("Generador de Números Pares")
    
    
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))
    
    if num1 % 2 == 1:
        num1 = num1 + 1  
        
    for num in range(num1, num2 + 1, 2):
        
        print(num, end=" ")
    print() 