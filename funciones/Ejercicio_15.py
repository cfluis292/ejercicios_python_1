
def inicializar_cola(tamano):
    cola = []  
    
    for i in range(tamano):
        cola.append("*")  
    return cola

if __name__ == "__main__":
    
    tamano_cola = int(input("¿Cuántos lugares tendrá la cola de espera?: "))
    fila = inicializar_cola(tamano_cola)
    
    print("Así se ven los espacios:")
    print(fila) 