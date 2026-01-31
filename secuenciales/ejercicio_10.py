parcial1 = float(input("Calificacion del parcial 1: "))
parcial2 = float(input("Calificacion del parcial 2: "))
parcial3 = float(input("Calificacion del parcial 3: "))
examen = float(input("Calificacion del examen: "))
trabajo = float(input("Calificacion del trabajo: "))

promedio = (parcial1 + parcial2 + parcial3) / 3
cfinal = (promedio * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print("Calificacion final: ", cfinal)