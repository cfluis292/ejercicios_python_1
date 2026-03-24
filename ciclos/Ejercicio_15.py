

if __name__ == "__main__":
    print("Prestamo")
    
    pagoacum = 0.0
    pago = 10.0
    
    
    for mes in range(1, 21):
        
        pago_acum += pago
        
        pago *= 2
        
    print(f"Al final de los 20 meses tuvo que pagar en total: ${pagoacum}") 