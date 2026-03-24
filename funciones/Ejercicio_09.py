
def convertirsegundos(h, m, s):

    segundos_totales = (h * 3600) + (m * 60) + s
    
    return segundos_totales

if __name__ == "__main__":
    
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    resultado = convertirsegundos(horas, minutos, segundos)
    
    print(f"\nEl tiempo total es de: {resultado} segundos.") 