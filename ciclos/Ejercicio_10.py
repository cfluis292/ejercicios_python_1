
if __name__ == "__main__":
    print("Tablas de multiplicar")

    for tabla in range(1, 6):
        print(f"Tabla del {tabla}")
        
        for num in range(1, 11):
            print(f"{tabla} * {num} = {tabla * num}")
    
        input("Presiona Enter para ver la siguiente tabla...")
        
    print("¡Terminaste todas las tablas!")  