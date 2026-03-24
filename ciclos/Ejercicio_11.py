
if __name__ == "__main__":
    print("Detector de Números Primos")
    
    es_primo = True
    
    numero_es_primo = int(input("Introduce un número para comprobar si es primo: "))
    
    limite = int(numero_es_primo ** 0.5) + 1
    
    
    for num in range(2, limite):
        
        if numero_es_primo % num == 0:
            es_primo = False 
            break    

    if es_primo and numero_es_primo > 1:
        print("¡Es Primo!")
    else:
        print("No es Primo") 