

if __name__ == "__main__":
    print("Calculadora de Ahorro Anual")
    
    
    ahorro_acum = 0.0  
    
    for mes in range(1, 13):
        
        cant_mensual = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: $"))
        
        ahorro_acum = ahorro_acum + cant_mensual
        
        print(f"En el mes {mes} llevas ahorrado un total de: ${ahorro_acum}")
        
    print("========================================")
    print("¡Año terminado! Tu ahorro total fue de: ${ahorro_acum}") 