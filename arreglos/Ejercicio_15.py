equipos = []
resultados = []

for i in range(15):
    equipo1 = input(f"Introduce el nombre del equipo {i+1}: ")
    equipo2 = input(f"Introduce el nombre del otro equipo {i+1}: ")
    equipos.append([equipo1, equipo2])
    
    goles1 = int(input(f"Introduce los goles {equipo1}: "))
    goles2 = int(input(f"Introduce los goles del otro {equipo2}: "))
    resultados.append([goles1, goles2])

print("quiniela")
print("========")

for i in range(15):
    if resultados[i][0] > resultados[i][1]:
        resultado_quiniela = "1"
    elif resultados[i][0] < resultados[i][1]:
        resultado_quiniela = "2"
    else:
        resultado_quiniela = "X"
        
    print(f"{equipos[i][0]} - {equipos[i][1]} -> {resultado_quiniela}")