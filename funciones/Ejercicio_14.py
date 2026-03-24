

def inicializar_pila(pila):
    pila = []  
    
    for i in range(pila):
        pila.append(" :) ")  
    return pila

if __name__ == "__main__":
    print("--- Inicializador de Pilas ---")
    
 
    tamano = int(input("¿De qué tamaño quieres crear la pila?: "))
    mi_pila = inicializar_pila(tamano)
    
    print("Queda asi:")
    print(mi_pila) 